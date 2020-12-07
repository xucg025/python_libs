# -*- coding: utf-8 -*-
# @author: Spark
# @file: mapper.py.py
# @ide: PyCharm
# @time: 2020-12-07 17:43:01

import sys

for line in sys.stdin:
    words = line.strip().split('|')
    for word in words:
        print(word)
