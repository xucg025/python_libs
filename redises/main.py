# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-05-22 17:18:48

import redis

client = redis.StrictRedis()

pipe = client.pipeline(transaction=True)
pipe.incr('books')
pipe.set('books_a', 'ddd')
pipe.incr('books_a')
pipe.incr('books')
values = pipe.execute()
print(values)