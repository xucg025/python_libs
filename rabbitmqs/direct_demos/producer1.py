# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

import json
from rabbitmqs.producer import Producer

#  这种工作模式的原理是消息发送至exchange，exchange根据路由键（routing_key）转发到相对应的queue上。
#  可以使用默认exchange =' ' ，也可以自定义exchange
#  这种模式下不需要将exchange和任何进行绑定，当然绑定也是可以的。可以将exchange和queue，routing_key和queue进行绑定
#  传递或接受消息时 需要指定routing_key
#  需要先启动订阅者，此模式下的队列是consumer随机生成的，发布者仅仅发布消息到exchange，由exchange转发消息至 queue。


if __name__ == '__main__':
    producer = Producer('127.0.0.1', 5672, 'guest', 'guest', exchange_name='direct_exchange_test',
                        exchange_type='direct')
    routing_keys = ['direct_routing_key_1', 'direct_routing_key_2']
    for i in range(10):
        message = json.dumps({'OrderId': "1000%s" % i})
        routing_key = routing_keys[i % 2]
        producer.produce(message, 2, routing_key)
    producer.close()
