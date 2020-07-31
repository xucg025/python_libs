# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:02

import pika

exchange_name = 'python-direct-test'

config = pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
# 创建临时队列，队列名传空字符，consumer关闭后，队列自动删除
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue

queue_name = 'direct_queue_test_1'
channel.queue_declare(queue_name, durable=True)

# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='direct')
# 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='direct_key_1')


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    # time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # ch.basic_nack(method.delivery_tag)
    print(body.decode())


# channel.basic_qos(prefetch_count=1)
# 告诉rabbitmq，用callback来接受消息
channel.basic_consume(queue_name, callback, auto_ack=False)
channel.start_consuming()


# class Consumer(object):
#     def __init__(self):
#         self.conn = ConnFactory(**conn_config)
#         self.channel = self.conn.get_channel()
#         self.exchange_name = mq_config['direct']['exchange_name']
#         self.queue_name = 'direct_queue_test_10'
#         self.channel.exchange_declare(self.exchange_name, durable=True, exchange_type=mq_config['direct']['type'])
#         self.channel.queue_declare(queue=self.queue_name)
#         self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='direct_key_1')
#         self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='direct_key_2')
#         self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='direct_key_0')
#
#     def callback(self, ch, method, properties, body):
#         routing_key = method.routing_key
#         print("{}--->{}".format(method.routing_key, body.decode()))
#         ch.basic_ack(delivery_tag=method.delivery_tag)
#
#         # import time
#         # time.sleep(100)
#         # if routing_key == u'direct_key_0':
#         #     import time
#         #     i = 0
#         #     while True:
#         #         if i >= 0:
#         #             break
#         #         time.sleep(1)
#         #         i += 1
#         #         print(i)
#
#     def consume(self):
#         # 设置成False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
#         self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=False)
#         self.channel.start_consuming()
#
#
# if __name__ == '__main__':
#     print('consumer 0 starting...')
#     consumer = Consumer()
#     consumer.consume()