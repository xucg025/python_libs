# -*- coding: utf-8 -*-
# @author: Spark
# @file: topic_producer.py
# @ide: PyCharm
# @time: 2019-11-08 17:10:39

import pika

EXCHANGE_NAME = 'topic_exchange'

config = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(config)

channel = connection.channel()

# 创建模糊匹配的exchange
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')

# 这里关键字必须为点号隔开的单词，以便于消费者进行匹配。
routing_key = '[warn].kern'

message = 'Hello World!'
channel.basic_publish(exchange=EXCHANGE_NAME, routing_key=routing_key, body=message)

print('[生产者] Send %r:%r' % (routing_key, message))
connection.close()

