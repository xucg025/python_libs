# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

import json
from rabbitmqs.parent import Parent

# 这种模式下，传递到 exchange 的消息将会转发到所有与其绑定的 queue 上。

# 不需要指定 routing_key ，即使指定了也是无效。
# 需要提前将 exchange 和 queue 绑定，一个 exchange 可以绑定多个 queue，一个queue可以绑定多个exchange。
# 需要先启动 订阅者，此模式下的队列是 consumer 随机生成的，发布者 仅仅发布消息到 exchange ，由 exchange 转发消息至 queue。


class Producer(Parent):
    def __init__(self, host, port, username, password, exchange_name='', exchange_type='', queue_name='', routing_key=''):
        super(Producer, self).__init__(host, port, username, password, exchange_name, exchange_type,
                                       queue_name, routing_key)
        self.exchange_declare()

    def produce(self):
        for i in range(10):
            message = json.dumps({'OrderId': "1000%s" %i})
            super(Producer, self).produce(message, 2)


if __name__ == '__main__':
    producer = Producer('127.0.0.1', 5672, 'guest', 'guest', exchange_name='fanout_exchange_test', exchange_type='fanout')
    producer.produce()
    producer.close()
