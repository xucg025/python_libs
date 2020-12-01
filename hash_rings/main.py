# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-11-04 11:30:12

from hash_ring.hash_ring import HashRing

memcache_servers = ['192.168.0.246:11212',
                    '192.168.0.247:11212',
                    '192.168.0.249:11212']

ring = HashRing(memcache_servers)
server = ring.get_node('my_key')
print(server)