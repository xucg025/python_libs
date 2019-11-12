# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

import json, pika
from rabbitmqs.rabbit_config import conn_config, mq_config
from rabbitmqs.conn_factory import ConnFactory

# 这种模式下，传递到 exchange 的消息将会转发到所有与其绑定的 queue 上。

# 不需要指定 routing_key ，即使指定了也是无效。
# 需要提前将 exchange 和 queue 绑定，一个 exchange 可以绑定多个 queue，一个queue可以绑定多个exchange。
# 需要先启动 订阅者，此模式下的队列是 consumer 随机生成的，发布者 仅仅发布消息到 exchange ，由 exchange 转发消息至 queue。


class Producer(object):
    def __init__(self):
        self.conn = ConnFactory(**conn_config)
        self.channel = self.conn.get_channel()
        self.exchange_name = mq_config['fanout']['exchange_name']
        self.channel.exchange_declare(self.exchange_name, durable=True, exchange_type=mq_config['fanout']['type'])

    def close(self):
        self.conn.close()

    def produce(self, msg):
        # delivery_mode = 2 声明消息在队列中持久化，delivery_mod = 1 消息非持久化。
        self.channel.basic_publish(exchange=self.exchange_name, body=msg, routing_key='',
                                   properties=pika.BasicProperties(delivery_mode=2))


if __name__ == '__main__':
    producer = Producer()
    for i in range(20):
        message = json.dumps({'OrderId': "1000%s" % i})
        producer.produce(message)
    producer.close()


