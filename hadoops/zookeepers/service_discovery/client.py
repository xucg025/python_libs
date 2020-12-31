# -*- coding: utf-8 -*-
# @author: Spark
# @file: client.py
# @ide: PyCharm
# @time: 2020-12-22 10:34:10

import random
import sys
import time
import json
import socket

from kazoo.client import KazooClient


# 客户端连接zk,并从zk获取可用的服务器列表
class ZKClient(object):
    def __init__(self):
        self._zk = KazooClient(hosts='192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181')
        self._zk.start()
        self._get_servers()

    def _get_servers(self, event=None):
        """
        从zookeeper获取服务器地址信息列表
        """
        servers = self._zk.get_children('/rpc', watch=self._get_servers)
        # print(servers)
        self._servers = []
        for server in servers:
            data = self._zk.get('/rpc/' + server)[0]
            if data:
                addr = json.loads(data.decode())
                self._servers.append(addr)

    def _get_server(self):
        """
        随机选出一个可用的服务器
        """
        return random.choice(self._servers)

    def get_connection(self):
        """
        提供一个可用的tcp连接
        """
        sock = None
        while True:
            server = self._get_server()
            print('server:%s' % server)
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((server['host'], server['port']))
            except ConnectionRefusedError:
                time.sleep(1)
                continue
            else:
                break
        return sock


if __name__ == '__main__':
    # 模拟多个客户端批量生成任务，推送给服务器执行
    client = ZKClient()
    for i in range(40):
        sock = client.get_connection()
        sock.send(bytes(str(i), encoding='utf8'))
        sock.close()
        time.sleep(1)