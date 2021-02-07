# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-11-25 09:59:14

from elasticsearch import Elasticsearch

import sys
print("print1：",sys.getdefaultencoding())
name ="中国"
name = name.encode("utf-8")
print('name_utf8', name)
print("print2：",type(name))
name = name.decode("utf-8")
name = name.encode("gbk")
print('name_gbk', name)
print("print4：",type(name))