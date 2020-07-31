# -*- coding: utf-8 -*-
# @author: Spark
# @file: hello.py
# @ide: PyCharm
# @time: 2020-05-11 14:10:47

from nameko.rpc import rpc
import time


class GreetingService:
    name = "greeting_service"

    @rpc
    def hello(self, name):
        # time.sleep(10)
        return "Hello, {}!".format(name)
