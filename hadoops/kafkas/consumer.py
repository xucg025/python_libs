# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer.py
# @ide: PyCharm
# @time: 2020-12-02 17:13:45

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(bootstrap_servers='192.168.174.30:9092,192.168.174.31:9092,192.168.174.32:9092',
                         value_deserializer=lambda m: json.loads(m.decode()))
consumer.subscribe(topics=['topic8', 'topic_1'])
i = 0
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    i += 1
    print('i--->{}'.format(i), recv)
