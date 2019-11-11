# -*- coding: utf-8 -*-
# @author: Spark
# @file: topic_consumer.py
# @ide: PyCharm
# @time: 2019-11-08 17:10:48


import pika
import sys

EXCHANGE_NAME = 'topic_exchange'
QUEUE_NAME = 'topic_queue'

config = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(config)

channel = connection.channel()
channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type='topic')

result = channel.queue_declare(QUEUE_NAME)
queue_name = result.method.queue

#绑定键。‘#’匹配所有字符，‘*’匹配一个单词
binding_keys = ['[warn].*', 'info.*']

if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange=EXCHANGE_NAME, queue=queue_name, routing_key=binding_key)

print('[*] Writing for logs. To exit press CTRL+C.')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(queue=result.method.queue, on_message_callback=callback, auto_ack=False)

channel.start_consuming()