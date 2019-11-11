# -*- coding: utf-8 -*-
# @author: Spark
# @file: parent.py
# @ide: PyCharm
# @time: 2019-11-11 13:16:39
import pika


class Parent(object):
    def __init__(self, host, port, username, password,
                 exchange_name='', exchange_type='', queue_name='', routing_key=''):
        config = pika.ConnectionParameters(host=host, port=port, credentials=pika.PlainCredentials(username, password))
        # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
        self.connection = pika.BlockingConnection(config)
        self.channel = self.connection.channel()
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.queue_name = queue_name
        self.routing_key = routing_key

    def exchange_declare(self):
        # 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
        self.channel.exchange_declare(exchange=self.exchange_name, durable=True, exchange_type=self.exchange_type)

    def queue_bind(self):
        result = self.channel.queue_declare(queue=self.queue_name)
        # 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
        self.channel.queue_bind(exchange=self.exchange_name, queue=result.method.queue)

    def produce(self, message, delivery_mode=2):
        # 向队列插入数值 routing_key是队列名。delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化。routing_key 不需要配置
        self.channel.basic_publish(exchange=self.exchange_name, routing_key=self.routing_key, body=message,
                                   properties=pika.BasicProperties(delivery_mode=delivery_mode))

    def consume(self):
        # 设置成False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=False)
        self.channel.start_consuming()

    def callback(self):
        pass

    def close(self):
        self.connection.close()

