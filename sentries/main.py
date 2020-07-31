# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2019-12-23 16:44:36

# import sentry_sdk
# sentry_sdk.init("http://f116788436a14d42abb0e40ead55f4b1@192.168.174.28:9000/2")
# a = []
# print(a[111])

from raven import Client
client = Client('http://f116788436a14d42abb0e40ead55f4b1@192.168.174.28:9000/2')
client.captureMessage('my second exception')
try:
    a = []
    a[111]
except:
    client.captureException()
