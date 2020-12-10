# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:02

import pika, json

config = pika.ConnectionParameters(host='192.168.174.30', port=5672, virtual_host='vhost_test',
                                   credentials=pika.PlainCredentials('xucg', 'ajmd123'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
exchange_name = 'exchange-fanout-test'
queue_name = 'queue-fanout-test-1'
# 创建临时队列,队列名传空字符，consumer关闭后，队列自动删除
channel.queue_declare(queue_name)
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='fanout')
# 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
channel.queue_bind(exchange=exchange_name, queue=queue_name)

channel.basic_qos(prefetch_count=1)

i = 0


def callback(ch, method, properties, body):
    global i
    obj = json.loads(body.decode())

    if int(obj['OrderId']) == 5:
        ch.basic_nack(delivery_tag=method.delivery_tag)
    else:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())
    i += 1


channel.basic_consume(queue_name, callback, auto_ack=False)
channel.start_consuming()

