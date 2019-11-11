# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-11 15:06:11

from rabbitmqs.parent import Parent


class Producer(Parent):
    def __init__(self, host, port, username, password, exchange_name='', exchange_type='', queue_name=''):
        super(Producer, self).__init__(host, port, username, password, exchange_name, exchange_type, queue_name,)
        self.delivery_mode = 2
        self.exchange_declare()
