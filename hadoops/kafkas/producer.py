# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-12-02 16:57:59

from kafka import KafkaProducer
import json

# producer = KafkaProducer(bootstrap_servers=['192.168.174.30:9092'])
# future = producer.send('my_topic', key=b'my_key', value=b'my_value', partition= 0)
# result = future.get(timeout=10)
# print(result)

# producer = KafkaProducer(bootstrap_servers='192.168.174.30:9092', key_serializer=str.encode,
#                          value_serializer=str.encode)
producer = KafkaProducer(bootstrap_servers=['192.168.174.30:9092'], key_serializer=str.encode,
                         value_serializer=lambda m: json.dumps(m).encode())

msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test_1",
        "host": "xxxx",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
# msg = json.dumps(msg_dict)
for _ in range(100):
    producer.send('xcg', key='key{}'.format(_), value=msg_dict)
producer.close()
