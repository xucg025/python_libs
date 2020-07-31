# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:02

import pika

config = pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(config)
channel = connection.channel()

# 创建临时队列,队列名传空字符，consumer关闭后，队列自动删除
result = channel.queue_declare('', exclusive=True)
# 声明exchange，由exchange指定消息在哪个队列传递，如不存在，则创建。durable = True 代表exchange持久化存储，False 非持久化存储
channel.exchange_declare(exchange='python-test', durable=True, exchange_type='fanout')
# 绑定exchange和队列  exchange 使我们能够确切地指定消息应该到哪个队列去
channel.queue_bind(exchange='python-test', queue=result.method.queue)


# 定义一个回调函数来处理消息队列中的消息，这里是打印出来
def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())


# 设置成 False，在调用callback函数时，未收到确认标识，消息会重回队列。True，无论调用callback成功与否，消息都被消费掉
channel.basic_consume(result.method.queue, callback, auto_ack=False)
channel.start_consuming()

#
# channel.queue_declare(queue='python-test', durable=False)  # 申明消息队列，消息在这个队列传递，如果不存在，则创建队列
#
#
# # 定义一个回调函数来处理消息队列中的消息，这里是打印出来
# def callback(ch, method, properties, body):
#     ch.basic_ack(delivery_tag = method.delivery_tag)
#     print(body.decode())
#
# # 告诉rabbitmq，用callback来接收消息
# channel.basic_consume('python-test',callback)
# # 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理
# channel.start_consuming()
