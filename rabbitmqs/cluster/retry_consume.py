# -*- coding: utf-8 -*-
# @author: Spark
# @file: retry_consume.py
# @ide: PyCharm
# @time: 2020-12-14 10:29:54

import pika, json

config = pika.ConnectionParameters(host='192.168.174.33', port=5672, virtual_host='vhost_test',
                                   credentials=pika.PlainCredentials('xucg', 'ajmd123'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
exchange_name = 'retry_exchange'
queue_name = 'retry_queue-test-0'
# 创建临时队列,队列名传空字符，consumer关闭后，队列自动删除

channel.queue_declare(queue_name, durable=True)
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='fanout')
# 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
channel.queue_bind(exchange=exchange_name, queue=queue_name)

channel.basic_qos(prefetch_count=1)


def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    obj = json.loads(body.decode())
    print(obj)
    # import time
    # time.sleep(1)


# 设置成 False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
channel.basic_consume(queue_name, callback, auto_ack=False)
channel.start_consuming()

