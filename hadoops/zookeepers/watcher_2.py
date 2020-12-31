# -*- coding: utf-8 -*-
# @author: Spark
# @file: watcher.py
# @ide: PyCharm
# @time: 2020-12-17 17:53:19

from kazoo.client import KazooClient
import time

zk = KazooClient(hosts='192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181')
zk.start()


def my_watch(*args, **kwargs):
    print(args, kwargs)
    servers = zk.get_children('/ip', watch=my_watch)
    for server in servers:
        host = zk.get('/ip/{}'.format(server))
        print(host)
    # print(v)


v = zk.get_children('/ip', watch=my_watch)
# print(v)

while True:
    time.sleep(5)

