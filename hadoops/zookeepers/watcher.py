# -*- coding: utf-8 -*-
# @author: Spark
# @file: watcher.py
# @ide: PyCharm
# @time: 2020-12-17 17:53:19

from kazoo.client import KazooClient
import time

zk = KazooClient(hosts='192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181')
zk.start()

ip = None


@zk.DataWatch('/watcher/a')
def my_func(*args):
    print(args)
    print('data_watch...')
    # print('data--->{}'.format(data))
    # global ip
    # if data:
    #     ip = data.decode()
    # if stat:
    #     print("Version is %s" % stat.version)


@zk.ChildrenWatch('/ip')
def my_func1(*args):
    print('child_watch...')
    print(args)


while True:
    time.sleep(5)
    print('ok')
    # print('ip--->{}'.format(ip))

