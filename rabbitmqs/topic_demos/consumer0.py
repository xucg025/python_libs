# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2019-11-11 14:05:02

import pika, time
exchange_name = 'exchange-topic-test'
queue_name = 'queue-topic-test-0'
config = pika.ConnectionParameters(host='localhost', port=5672, credentials=pika.PlainCredentials('guest', 'guest'))
connection = pika.BlockingConnection(config)
channel = connection.channel()
# result = channel.queue_declare('', exclusive=True)
# queue_name = result.method.queue
channel.exchange_declare(exchange=exchange_name, durable=True, exchange_type='topic')
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='like.#') # routing_ke队列指定以什么规则绑定交换和队列


def callback(channel, method, properties, body):
    try:
        print(body.decode())
        t = body.decode()
        if int(t)%2 == 0:
            return
        message_id = properties.message_id
        print('message_id--->{}'.format(message_id))
        # 1/0
        channel.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(e)

# channel.basic_qos(prefetch_count=1)
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