# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer2.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:10

from rabbitmqs.conn_factory import ConnFactory
from rabbitmqs.rabbit_config import conn_config, mq_config

import pika

config = pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(config)
channel = connection.channel()

exchange_name = 'python-test'

# 创建临时队列,队列名传空字符，consumer关闭后，队列自动删除
result = channel.queue_declare('', exclusive=True)
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='fanout')
# 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
channel.queue_bind(exchange=exchange_name, queue=result.method.queue)


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())


# 设置成 False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
channel.basic_consume(result.method.queue, callback, auto_ack=False)
channel.start_consuming()


# class Consumer(object):
#     def __init__(self):
#         self.conn = ConnFactory(**conn_config)
#         self.channel = self.conn.get_channel()
#         self.exchange_name = mq_config['fanout']['exchange_name']
#         self.queue_name = 'fanout_queue_test_2'
#         self.channel.exchange_declare(self.exchange_name, durable=True, exchange_type=mq_config['fanout']['type'])
#         self.channel.queue_declare(queue=self.queue_name)
#         self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name)
#
#     def callback(self, ch, method, properties, body):
#         ch.basic_ack(delivery_tag=method.delivery_tag)
#         import time
#         print("{}".format(body.decode()))
#         # time.sleep(10)
#
#     def consume(self):
#         # 设置成False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
#         self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=False)
#         self.channel.start_consuming()
#
#
# if __name__ == '__main__':
#     print('consumer 2 starting...')
#     consumer = Consumer()
#     consumer.consume()
