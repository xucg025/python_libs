# -*- coding: utf-8 -*-
# @author: Spark
# @file: distribute_lock.py
# @ide: PyCharm
# @time: 2020-01-02 10:54:17

import os
import time
import datetime
import threading
from kazoo.client import KazooClient


class ZkDistributedLock(object):
    """
    基于zk的临时顺序节点实现分布式锁
    """
    def __init__(self, hosts, locker_path, sub_node_name, timeout, default_value=b'1'):
        self.hosts = hosts
        # 持久节点路径
        self.locker_path = locker_path
        self.timeout = timeout
        # 子节点路径
        # self.sub_node_path = os.path.join(self.locker_path, sub_node_name)
        self.sub_node_path = self.locker_path + '/' + sub_node_name
        # 创建子节点为临时顺序节点的默认值（只需要有值就行）
        self.default_value = default_value

        # 用于客户端自己首次发起请求为获得锁后，用线程的事件阻塞自己不退出，继续等待zk的删除事件通知
        # 这比使用while True+time.sleep()方式更优雅
        self.thread_event = threading.Event()

        # 创建zk连接，若未创建成功，直接raise Kazoo定义的连接错误，这里无需再给出try except的错误。
        self.zkc = KazooClient(hosts=self.hosts, timeout=self.timeout)
        self.zkc.start(self.timeout)
        if not self.zkc.exists(self.locker_path):
            self.zkc.create(self.locker_path)

    def get_lock(self):
        # 这里是直接返回临时顺序节点的完整路径，例如返回：'/locker/foo0000000002'
        self.current_node_path = self.zkc.create(path=self.sub_node_path, value=self.default_value, ephemeral=True,
                                                 sequence=True)

        # 获取固定节点下的所有临时顺序节点列表
        all_nodes = self.zkc.get_children(self.locker_path)
        # 对临时顺序节点列表进行排序，小到大，kazoo返回是节点名称，不是路径：['foo0000000001','foo0000000002','foo0000000003'....]
        all_nodes = sorted(all_nodes)

        if len(all_nodes) == 1:
            # 如果仅有zk的/locker路径下仅有一个临时顺序节点，说明没有其他客户端争抢，本客户端直接获得锁
            d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('current node {0} got the locker at {1}'.format(self.current_node_path, d))
            # 线程阻塞事件被set为True，通知客户端无需再阻塞自己，已经获得锁。
            self.thread_event.set()
            return

        # 获取最小节点名例如'foo0000000001'
        min_node = all_nodes[0]
        # 拼接最小节点路径:'/locker/foo0000000001'
        # min_node_path = os.path.join(self.locker_path, min_node)
        min_node_path = self.locker_path + '/' + min_node

        # 如果自身节点为最小节点，说明获得锁，进行操作后可以是释放锁
        if self.current_node_path == min_node_path:
            d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('current node {0} got the locker at {1}'.format(self.current_node_path, d))
            self.thread_event.set()
            # 线程阻塞事件被set为True，通知客户端无需再阻塞自己，已经获得锁。
        else:
            # 当前节点不是最小节点，获取当前节点的前面的节点，并对该节点进行路径存在监听（注意这里不是对最小节点监听,避免羊群效应）
            current_node = os.path.split(self.current_node_path)[1]
            pre_node_index = all_nodes.index(current_node) - 1
            pre_node = all_nodes[pre_node_index]

            # 获得在当前节点前面的那个节点路径
            # self.pre_node_path = os.path.join(self.locker_path, pre_node)
            self.pre_node_path = self.locker_path + '/' + pre_node
            print('current node：{0} is watching the pre node：{1}'.format(self.current_node_path, self.pre_node_path))

            # 对当前节点前面的那个节点增加"exists事件"监听
            self.zkc.exists(path=self.pre_node_path, watch=self.watch_node_is_exist)

    def watch_node_is_exist(self, event):
        """当前节点前面的那个节点被删除，触发删除事件，该函数被回调，获得锁
        若
        :param event:
        :return:
        """
        if event:
            d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('current node {0} got the locker at {1}'.format(self.current_node_path, d))
            self.thread_event.set()
        else:
            pass

    def release(self):
        # 释放锁，通过删除当前子节点路径实现
        if self.zkc.exists(self.current_node_path):
            d = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print('deleted node {0} at {1}'.format(self.current_node_path, d))
            self.zkc.delete(self.current_node_path)
            self.zkc.stop()
            self.zkc.close()

    def __enter__(self):
        # 客户端首次发起请求锁，线程事件为False
        if not self.thread_event.is_set():
            # 去zk获取锁
            self.get_lock()
            # 如果本客户端首次请求锁却未能获得，那么客户端可以阻塞自己不退出，这里没限制重新获取锁的次数
            # （也可以设计为retry次数到达前，阻塞自己，超过retry次数后，客户端退出并提示获取锁失败）
            self.thread_event.wait()
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()


def doing_jobs(a, b):
    """
    模拟业务处理逻辑
    :param a:
    :param b:
    :return:
    """
    c = a + b
    print('doing jobs')
    time.sleep(5)
    print('jobs is done!')
    return c


def run():
    conf = {
        'hosts': '192.168.174.28:2183',
        'locker_path': '/locker',
        'sub_node_name': 'foo',
        'timeout': 5
    }

    with ZkDistributedLock(**conf):
        doing_jobs(1, 2)


if __name__ == '__main__':
    run()
