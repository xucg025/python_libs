# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-12 16:09:33

from rediscluster import RedisCluster

startup_nodes = [{'host': '192.168.174.29', 'port': 7000},
                 {'host': '192.168.174.29', 'port': 7001},
                 {'host': '192.168.174.29', 'port': 7002},
                 {'host': '192.168.174.29', 'port': 7003},
                 {'host': '192.168.174.29', 'port': 7004},
                 {'host': '192.168.174.29', 'port': 7005}]


rc = RedisCluster(startup_nodes=startup_nodes)
rc.set('foo', 'bar')
print(rc.get('foo'))