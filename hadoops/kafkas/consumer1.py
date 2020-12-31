# -*- coding: utf-8 -*-
# @author: Spark
# @file: consumer1.py
# @ide: PyCharm
# @time: 2020-12-02 18:45:42

from kafka import KafkaConsumer
from kafka.structs import TopicPartition

consumer = KafkaConsumer(group_id='123456', bootstrap_servers='192.168.174.30:9092,192.168.174.31:9092,192.168.174.32:9092')
consumer.assign([TopicPartition(topic='topic8', partition=0), TopicPartition(topic='topic8', partition=2)])
# print(consumer.partitions_for_topic("topic8"))  # 获取topic8主题的分区信息
# print(consumer.assignment())
# print(consumer.beginning_offsets(consumer.assignment()))
consumer.seek(TopicPartition(topic='topic8', partition=2), 462272)
consumer.seek(TopicPartition(topic='topic8', partition=0), 99997)
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)