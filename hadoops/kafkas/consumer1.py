# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2020-12-02 18:45:42

from kafka import KafkaConsumer
from kafka.structs import TopicPartition

consumer = KafkaConsumer(group_id='123456', bootstrap_servers=['192.168.174.30:9092'])
consumer.assign([TopicPartition(topic='xcg_test', partition=0), TopicPartition(topic='xcg_test', partition=2)])
print(consumer.partitions_for_topic("xcg_test"))  # 获取test主题的分区信息
print(consumer.assignment())
print(consumer.beginning_offsets(consumer.assignment()))
consumer.seek(TopicPartition(topic='xcg_test', partition=2), 32850)
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)