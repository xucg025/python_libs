# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-12-02 16:57:59

from kafka import KafkaProducer
import json, time
from kafka.errors import kafka_errors

producer = KafkaProducer(bootstrap_servers='192.168.174.30:9092,192.168.174.31:9092,192.168.174.32:9092',
                         key_serializer=lambda m: json.dumps(m).encode(),
                         value_serializer=lambda m: json.dumps(m).encode())

# 方式一：发送并忘记(不关心消息是否正常到达，对返回结果不做任何判断处理)
# 发送并忘记的方式本质上也是一种异步的方式，只是它不会获取消息发送的返回结果，这种方式的吞吐量是最高的，但是无法保证消息的可靠性：
#
start_time = time.time()
for i in range(0, 10000):
    # print('------{}---------'.format(i))
    future = producer.send('topic8', key='num', value=i)

# 将缓冲区的全部消息push到broker当中
producer.flush()
producer.close()

end_time = time.time()
time_counts = end_time - start_time
print(time_counts)


# # 方式二：同步发送(通过get方法等待Kafka的响应，判断消息是否发送成功)
# #
# # 以同步的方式发送消息时，一条一条的发送，对每条消息返回的结果判断， 可以明确地知道每条消息的发送情况，但是由于同步的方式会阻塞，只有当消息通过get返回future对象时，才会继续下一条消息的发送：
# start_time = time.time()
# for i in range(0, 100000):
#     # print('------{}---------'.format(i))
#     future = producer.send(topic="topic8", key="num", value=i)
#     # 同步阻塞,通过调用get()方法进而保证一定程序是有序的.
#     try:
#         record_metadata = future.get(timeout=10)
#         # print(record_metadata.topic)
#         # print(record_metadata.partition)
#         # print(record_metadata.offset)
#     except kafka_errors as e:
#         print(str(e))
#
# end_time = time.time()
# time_counts = end_time - start_time
# print(time_counts)

# def on_send_success(*args, **kwargs):
#     """
#     发送成功的回调函数
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     return args
#
#
# def on_send_error(*args, **kwargs):
#     """
#     发送失败的回调函数
#     :param args:
#     :param kwargs:
#     :return:
#     """
#
#     return args
#
#
# start_time = time.time()
# for i in range(0, 100):
#     # print('------{}---------'.format(i))
#     # 如果成功,传进record_metadata,如果失败,传进Exception.
#     producer.send(
#         topic="topic8", key="num", value=i
#     ).add_callback(on_send_success).add_errback(on_send_error)
#
# producer.flush()
# producer.close()
#
# end_time = time.time()
# time_counts = end_time - start_time
# print(time_counts)