# -*- coding: utf-8 -*-
# @author: Spark
# @file: direct_producer.py
# @ide: PyCharm
# @time: 2019-11-08 11:39:32

# 这种工作模式的原理是消息发送至exchange，exchange根据路由键（routing_key）转发到相对应的queue上。
#  可以使用默认exchange =' ' ，也可以自定义exchange
#  这种模式下不需要将exchange和任何进行绑定，当然绑定也是可以的。可以将exchange和queue，routing_key和queue进行绑定
#  传递或接受消息时 需要指定routing_key
#  需要先启动订阅者，此模式下的队列是consumer随机生成的，发布者仅仅发布消息到exchange，由exchange转发消息至 queue。

import pika, json

EXCHANGE_NAME = 'direct_exchange'

config = pika.ConnectionParameters(host='127.0.0.1', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
# 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
connection = pika.BlockingConnection(config)

channel = connection.channel()

# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=EXCHANGE_NAME, durable=True, exchange_type='direct')

for i in range(10):
    message = json.dumps({'OrderId': "1000%s" %i})
# 指定 routing_key。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
    channel.basic_publish(exchange=EXCHANGE_NAME, routing_key='OrderId', body=message,
                          properties=pika.BasicProperties(delivery_mode=2))
    print(message)
connection.close()