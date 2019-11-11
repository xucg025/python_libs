# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

import json
from rabbitmqs.producer import Producer

# 这种模式下，传递到 exchange 的消息将会转发到所有与其绑定的 queue 上。

# 不需要指定 routing_key ，即使指定了也是无效。
# 需要提前将 exchange 和 queue 绑定，一个 exchange 可以绑定多个 queue，一个queue可以绑定多个exchange。
# 需要先启动 订阅者，此模式下的队列是 consumer 随机生成的，发布者 仅仅发布消息到 exchange ，由 exchange 转发消息至 queue。


if __name__ == '__main__':
    producer = Producer('127.0.0.1', 5672, 'guest', 'guest', exchange_name='fanout_exchange_test', exchange_type='fanout')
    for i in range(10):
        message = json.dumps({'OrderId': "1000%s" % i})
        producer.produce(message, delivery_mode=2)
    producer.close()
