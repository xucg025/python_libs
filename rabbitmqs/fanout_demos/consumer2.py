# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer2.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:10

from rabbitmqs.consumer import Consumer


if __name__ == '__main__':
    print('consumer 2 starting...')
    consumer = Consumer('127.0.0.1', 5672, 'guest', 'guest', exchange_name='fanout_exchange_test',
                        exchange_type='fanout', queue_name='fanout_queue_test_2')
    consumer.consume()
    consumer.close()
