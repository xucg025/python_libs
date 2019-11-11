# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:02

from rabbitmqs.consumer import Consumer


if __name__ == '__main__':
    print('consumer 1 starting...')
    consumer = Consumer('127.0.0.1', 5672, 'guest', 'guest', exchange_name='direct_exchange_test',
                        exchange_type='direct', queue_name='direct_queue_test_1', routing_key='direct_routing_key_1')
    consumer.consume()
    consumer.close()
