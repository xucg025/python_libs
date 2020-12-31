# -*- coding: utf-8 -*-
# @author: Spark
# @file: distribute_lock_2.py
# @ide: PyCharm
# @time: 2020-12-21 17:31:43

import logging, os, time
from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock


class ZKDistributedLock(object):
    def __init__(self, hosts, name, logger=None, timeout=1):
        """
        :param hosts: zookeeper主机地址
        :param name: 分布式锁名称
        :param logger: 日志对象
        :param timeout: 连接超时
        """
        self._client = None
        self._lock = None

        # 创建客户端对象并初始化连接
        try:
            self._client = KazooClient(hosts=hosts, logger=logger, timeout=timeout)
            self._client.start(timeout=timeout)
        except Exception as e:
            logging.error('Create KazooClient Failed! Exception:{}'.format(e))

        # 创建Lock对象
        try:
            lock_path = os.path.join("/", "locks", name)
            self._lock = Lock(self._client, lock_path)
        except Exception as e:
            logging.error('Create Lock Failed! Exception: %s'.format(e))

    def __enter__(self):
        """
        上下文管理器
        :return:
        """
        if not self.acquire():
            raise Exception('Get Lock Failed')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        上下文管理器
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.release()

    def __del__(self):
        """
        :return:
        """
        self.release()
        if self._client:
            self._client.stop()
            self._client = None

    def acquire(self, blocking=True, timeout=None):
        """
        获取锁
        :param blocking:
        :param timeout:
        :return:
        """
        if self._lock is None:
            return False

        try:
            return self._lock.acquire(blocking=blocking, timeout=timeout)
        except Exception as e:
            logging.error('Acquire lock failed! Exception: %s'.format(e))
            return False

    def release(self):
        """
        释放锁
        :return:
        """
        if self._lock is not None:
            self._lock.release()
            logging.info('Release Lock')


def main():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s -%(module)s:%(filename)s-L%(lineno)d-%(levelname)s: %(message)s')
    sh.setFormatter(formatter)
    logger.addHandler(sh)

    hosts = "192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181"
    name = "test"

    with ZKDistributedLock(hosts, name, logger=logger) as lock:
        logging.info('Get lock ok,  sleep 10s')
        for i in range(1, 11):
            time.sleep(1)
            print(str(i))

        logging.info('Release lock')
        lock.release()


if __name__ == "__main__":
    main()

