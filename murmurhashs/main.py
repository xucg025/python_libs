# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2021-01-21 15:16:06

url = 'https://github.com/wangzheng0822/ratelimiter4j'

import mmh3
v = mmh3.hash(url)
print(v)