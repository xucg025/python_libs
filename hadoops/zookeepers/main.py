# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-12-17 10:03:28

# from kazoo.client import KazooClient
#
# zk = KazooClient(hosts='192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181')
# zk.start()

import time
from kazoo.client import KazooClient
from kazoo.client import ChildrenWatch


zk = KazooClient(hosts='192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181')
zk.start()
# zk.get_children()
# zk.set('/watcher/a', 'this is a test1'.encode())
zk.create('/ip/server', value='192.168.1.0:8080'.encode(), ephemeral=False, sequence=True, makepath=True)
zk.stop()
zk.close()

