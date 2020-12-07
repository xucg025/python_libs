# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer3.py
# @ide: PyCharm
# @time: 2020-12-02 18:51:24

from kafka import KafkaConsumer
import time

consumer = KafkaConsumer(group_id='123456', bootstrap_servers=['192.168.174.30:9092'])
consumer.subscribe(topics=('xcg_test',))
index = 0
while True:
    msg = consumer.poll(timeout_ms=5)  # 从kafka获取消息
    print(msg)
    print('\n')
    time.sleep(2)
    index += 1
    print('--------poll index is %s----------' % index)