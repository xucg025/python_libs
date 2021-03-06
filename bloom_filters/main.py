# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-05-13 18:45:30

# from pybloom_live import BloomFilter, ScalableBloomFilter
#
# bf = BloomFilter(capacity=10000, error_rate=0.1)
#
# bf.add("www.baidu.com")
# bf.add(123)
# bf.add(124)
# print("www.baidu.com" in bf)   # True
# print("www.douban.com" in bf)  # False
#
# print(bf.__getstate__())
# #
# # sbf = ScalableBloomFilter(initial_capacity=100, error_rate=0.001, mode=ScalableBloomFilter.LARGE_SET_GROWTH)
# #
# # url = "www.baidu.com"
# # url2 = "www.douban,com"
# #
# # sbf.add(url)
# #
# # print(url in sbf)   # True
# # print(url2 in sbf)  # False

import redis
client = redis.StrictRedis(host='192.168.174.30', port=6380)
client.delete("codehole")
for i in range(10000):
    client.execute_command("bf.add", "codehole", "user%d" % i)
    ret = client.execute_command("bf.exists", "codehole", "user%d" % i)
    if ret == 0:
        print(i)
        break
