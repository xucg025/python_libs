# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer.py
# @ide: PyCharm
# @time: 2019-11-08 17:04:21

from rabbitmqs.parent import Parent


class Consumer(Parent):
    def __init__(self, host, port, username, password, exchange_name='', exchange_type='', queue_name='', routing_key=''):
        super(Consumer, self).__init__(host, port, username, password, exchange_name, exchange_type, queue_name)
        self.exchange_declare()
        self.queue_declare()
        self.queue_bind(routing_key)

    def callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(body.decode())


