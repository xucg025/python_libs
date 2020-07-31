# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

#  这种工作模式的原理是消息发送至exchange，exchange根据路由键（routing_key）转发到相对应的queue上。
#  可以使用默认exchange =' ' ，也可以自定义exchange
#  这种模式下不需要将exchange和任何进行绑定，当然绑定也是可以的。可以将exchange和queue，routing_key和queue进行绑定
#  传递或接受消息时 需要指定routing_key
#  需要先启动订阅者，此模式下的队列是consumer随机生成的，发布者仅仅发布消息到exchange，由exchange转发消息至 queue。

import pika
import uuid
import json

exchange_name = 'exchange-topic-test'
config = pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='topic')
# channel.basic_publish(exchange=exchange_name, routing_key='a.b.c.d', body='Hello topic')
properties = pika.BasicProperties(delivery_mode=2)
properties.content_type = 'text/plain'


for i in range(10000):
    message = f'{i}'
    properties.message_id = str(uuid.uuid1())
    # properties.expiration = '1000000'
    print('message_id--->{}'.format(properties.message_id))
    if i % 2 == 0:
        channel.basic_publish(exchange=exchange_name, routing_key='like.you', body=message, properties=properties)
    else:
        channel.basic_publish(exchange=exchange_name, routing_key='hate.you', body=message, properties=properties)
    print(message)
connection.close()


# for i in range(10):
#     message = json.dumps({'OrderId': "1000%s" % i})
#     routing_key = 'direct_key_{}'.format(i % 2)
#     # routing_key = 'direct_key'
# # 指定 routing_key。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化
#     channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message,
#                           properties=pika.BasicProperties(delivery_mode=2))
#     print(message)
# connection.close()


# class Producer(object):
#     def __init__(self):
#         self.conn = ConnFactory(**conn_config)
#         self.channel = self.conn.get_channel()
#         self.exchange_name = mq_config['direct']['exchange_name']
#         self.channel.exchange_declare(self.exchange_name, durable=True, exchange_type=mq_config['direct']['type'])
#
#     def close(self):
#         self.conn.close()
#
#     def produce(self, msg, routing_key):
#         # delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化。
#         self.channel.basic_publish(exchange=self.exchange_name, body=msg, routing_key=routing_key,
#                                    properties=pika.BasicProperties(delivery_mode=2))
#
#
# if __name__ == '__main__':
#     producer = Producer()
#     for i in range(20):
#         routing_key = 'direct_key_{}'.format(i % 5)
#         message = json.dumps({'OrderId': "1000%s" % i})
#         print(message)
#         producer.produce(message, routing_key)
#     producer.close()
