# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

# import json, pika
# # from rabbitmqs.rabbit_config import conn_config, mq_config
# from rabbitmqs.conn_factory import ConnFactory

#  这种工作模式的原理是消息发送至exchange，exchange根据路由键（routing_key）转发到相对应的queue上。
#  可以使用默认exchange =' ' ，也可以自定义exchange
#  这种模式下不需要将exchange和任何进行绑定，当然绑定也是可以的。可以将exchange和queue，routing_key和queue进行绑定
#  传递或接受消息时 需要指定routing_key
#  需要先启动订阅者，此模式下的队列是consumer随机生成的，发布者仅仅发布消息到exchange，由exchange转发消息至 queue。

import pika
import json

exchange_name = 'exchange-direct-test'
config = pika.ConnectionParameters(host='192.168.174.31', port=5672, virtual_host='vhost_test',
                                   credentials=pika.PlainCredentials('xucg', 'ajmd123'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='direct')

# = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
for i in range(10):
    message = json.dumps({'OrderId': "%s" % i})
    routing_key = 'direct_key_{}'.format(i % 2)
    # routing_key = 'direct_key_1'
    properties = pika.BasicProperties(delivery_mode=2, headers={'message_num': i})  # delivery_mode
    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message,
                          properties=properties, mandatory=True)
    print(message)
connection.close()
