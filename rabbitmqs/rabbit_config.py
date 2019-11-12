# -*- coding: utf-8 -*-
# @author: Spark
# @file: rabbit_config.py
# @ide: PyCharm
# @time: 2019-11-12 17:06:15

conn_config = {'host': 'localhost', 'port': 5672, 'username': 'guest', 'password': 'guest'}

mq_config = {'fanout': {'exchange_name': 'fanout_exchange_test', 'type': 'fanout'},
             'direct': {'exchange_name': 'direct_exchange_test', 'type': 'direct'}}
