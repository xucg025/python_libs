# -*- coding: utf-8 -*-
# @author: Spark
# @file: producer1.py
# @ide: PyCharm
# @time: 2019-11-08 16:58:59

# 这种模式下，传递到 exchange 的消息将会转发到所有与其绑定的 queue 上。

# 不需要指定 routing_key ，即使指定了也是无效。
# 需要提前将 exchange 和 queue 绑定，一个 exchange 可以绑定多个 queue，一个queue可以绑定多个exchange。
# 需要先启动 订阅者，此模式下的队列是 consumer 随机生成的，发布者 仅仅发布消息到 exchange ，由 exchange 转发消息至 queue。

import pika, json

config = pika.ConnectionParameters(host='192.168.174.30', port=5672, virtual_host='vhost_test',
                                   credentials=pika.PlainCredentials('xucg', 'ajmd123'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
channel.confirm_delivery()
exchange_name = 'exchange-fanout-test'
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='fanout', auto_delete=False, passive=False)

for i in range(100000):
    try:
        message = json.dumps({'OrderId': "%s" % i})
        print(message)
        # 向队列插入数值 routing_key是队列名。delivery_mode = 2 声明消息在队列中持久化，
        # delivery_mod = 1 消息非持久化。routing_key 不需要配置
        # channel.tx_select()
        channel.basic_publish(exchange=exchange_name, routing_key='', body=message,
                              properties=pika.BasicProperties(delivery_mode=2, expiration='50000000',
                                                              message_id='orderId::{}'.format(i)))

        # 1/0
        # channel.tx_commit()
        #
        # properties = pika.BasicProperties(delivery_mode=2)
        # properties.content_type = 'text/plain'
        # # channel.basic_publish(exchange=exchange_name, routing_key='', body=message, properties=properties)
        # channel.basic_publish(exchange=exchange_name, routing_key='', body=message, properties=properties)
        # if ack:
        #     print('push message to broker succeed')
        # else:
        #     print('push message to broker failed')
    except Exception as e:
        print(e)
        # channel.tx_rollback()
connection.close()



