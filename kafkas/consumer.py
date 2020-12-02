# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer.py
# @ide: PyCharm
# @time: 2020-12-02 17:13:45

from kafka import KafkaConsumer

consumer = KafkaConsumer('xcg', bootstrap_servers=['192.168.174.30:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)
