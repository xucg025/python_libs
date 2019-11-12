# -*- coding: utf-8 -*-
# @author: Spark
# @file: conn_factory.py
# @ide: PyCharm
# @time: 2019-11-12 16:58:47
import pika


class ConnFactory(object):
    def __init__(self, host, port, username, password):
        config = pika.ConnectionParameters(host=host, port=port, credentials=pika.PlainCredentials(username, password))
        # 虚拟队列需要指定参数 virtual_host，如果是默认的可以不填。
        self.connection = pika.BlockingConnection(config)

    def get_channel(self):
        return self.connection.channel()

    def close(self):
        if self.connection:
            self.connection.close()
