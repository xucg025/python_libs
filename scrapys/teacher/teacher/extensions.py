# -*- coding: utf-8 -*-
# @author: Spark
# @file: extensions.py
# @ide: PyCharm
# @time: 2021-02-07 17:10:38

from scrapy import signals


class MyExtension(object):
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls()
        crawler.signals.connect(obj.func_1, signal=signals.spider_opened)
        crawler.signals.connect(obj.func_2, signal=signals.spider_closed)
        return obj

    def func_1(self):
        print('func_1,,,,')

    def func_2(self):
        print('func_2,,,,')
