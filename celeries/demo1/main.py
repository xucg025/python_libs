# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2019-11-13 09:47:28

from tasks import add

for i in range(100000):
    add.delay(i, i+1)