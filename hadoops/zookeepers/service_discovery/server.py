# -*- coding: utf-8 -*-
# @author: Spark
# @file: server.py
# @ide: PyCharm
# @time: 2020-12-22 10:34:22

import threading
import json
import socket
import sys
from kazoo.client import KazooClient


# TCP服务端绑定端口开启监听，同时将自己注册到zk
class ZKServer(object):
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = port
        self.sock.bind((host, port))
        self.zk = None

    def serve(self):
        """
        开始服务，每次获取得到一个信息，都新建一个线程处理
        """
        self.sock.listen(128)
        self.register_zk()
        print("开始监听")
        while True:
            conn, addr = self.sock.accept()
            print("建立链接%s" % str(addr))
            t = threading.Thread(target=self.handle, args=(conn, addr))
            t.start()

    # 具体的处理逻辑,只要接收到数据就立即投入工作，下次没有数据本次链接结束
    def handle(self, conn, addr):
        while True:
            data=conn.recv(1024)
            if not data or data.decode('utf-8') == 'exit':
                break
            print(data.decode('utf-8'))
        conn.close()
        print('My work is done!!!')

    # 将自己注册到zk，临时节点，所以连接不能中断
    def register_zk(self):
        """
        注册到zookeeper
        """
        self.zk = KazooClient(hosts='192.168.174.30:2181,192.168.174.31:2181,192.168.174.32:2181')
        self.zk.start()
        self.zk.ensure_path('/rpc')  # 创建根节点
        value = json.dumps({'host': self.host, 'port': self.port})
        # 创建服务子节点
        self.zk.create('/rpc/server', value.encode(), ephemeral=True, sequence=True)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage:python server.py [host] [port]")
        exit(1)
    host = sys.argv[1]
    port = sys.argv[2]
    server = ZKServer(host, int(port))
    server.serve()