# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer2.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:10

from rabbitmqs.conn_factory import ConnFactory
from rabbitmqs.rabbit_config import conn_config, mq_config


class Consumer(object):
    def __init__(self):
        self.conn = ConnFactory(**conn_config)
        self.channel = self.conn.get_channel()
        self.exchange_name = mq_config['direct']['exchange_name']
        self.queue_name = 'direct_queue_test_2'
        self.channel.exchange_declare(self.exchange_name, durable=True, exchange_type=mq_config['direct']['type'])
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='direct_key_3')
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='direct_key_4')
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key='direct_key_0')

    def callback(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("{}--->{}".format(method.routing_key, body.decode()))

    def consume(self):
        # 设置成False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=False)
        self.channel.start_consuming()


if __name__ == '__main__':
    print('consumer 2 starting...')
    consumer = Consumer()
    consumer.consume()