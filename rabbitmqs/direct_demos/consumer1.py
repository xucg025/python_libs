# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:02

# from rabbitmqs.conn_factory import ConnFactory
# from rabbitmqs.rabbit_config import conn_config, mq_config

import pika, time, json

count = 0

exchange_name = 'exchange-direct-test'

config = pika.ConnectionParameters(host='192.168.174.30', port=5672, virtual_host='vhost_test',
                                   credentials=pika.PlainCredentials('xucg', 'ajmd123'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
# 创建临时队列，队列名传空字符，consumer关闭后，队列自动删除
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue

queue_name = 'queue-direct-test-1'
queue = channel.queue_declare(queue_name, durable=True)

# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='direct')
# 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='direct_key_1')
channel.basic_qos(prefetch_count=1)

# 定义一个回调函数来处理消息队列中的消息，这里是打印出来

def callback(ch, method, properties, body):
    obj = json.loads(body.decode())
    print('obj--->{}'.format(obj))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue_name, callback, auto_ack=False)
channel.start_consuming()


