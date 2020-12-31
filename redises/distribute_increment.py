# -*- coding: utf-8 -*-
# @author: Spark
# @file: distribute_increment.py
# @ide: PyCharm
# @time: 2020-12-20 11:42:26

import redis

client = redis.StrictRedis()

list_name = 'test_count_list'
inc = 100
len = client.llen(list_name)


def increment():
    client.incrby('test_count', inc)


if len > 0:
    content = client.lpop('test_count_list')
    if content:
        print(content)
    else:
        increment()
else:
    increment()