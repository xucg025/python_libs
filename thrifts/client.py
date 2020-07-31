# -*- coding: utf-8 -*-
# @author: Spark
# @file: client.py
# @ide: PyCharm
# @time: 2020-06-17 17:37:01


# import sys
#
# sys.path.append('./gen-py')
#
# from service import HelloWorld, Printer
# from service.ttypes import *
# from service.constants import *
#
# from thrift import Thrift
# from thrift.transport import TSocket
# from thrift.transport import TTransport
# from thrift.protocol import TBinaryProtocol
# from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol
#
# if __name__ == '__main__':
#     try:
#         # Make socket
#         transport = TSocket.TSocket('127.0.0.1', 30303)
#         # Buffering is critical. Raw sockets are very slow
#         transport = TTransport.TBufferedTransport(transport)
#         # Wrap in a protocol
#         protocol = TBinaryProtocol.TBinaryProtocol(transport)
#         # 注册两个protocol 如果想要实现单端口 多服务 就必须使用 TMultiplexedProtocol
#         printer_protocol = TMultiplexedProtocol(protocol, 'printer')
#         hello_world_protocol = TMultiplexedProtocol(protocol, 'hello_world')
#         # # Create a client to use the protocol encoder
#         # client = HelloWorld.Client(protocol)
#
#         # 注册两个客户端
#         printer_client = Printer.Client(printer_protocol)
#         hello_world_client = HelloWorld.Client(hello_world_protocol)
#         transport.open()
#
#         hello_world_client.ping()
#         print("ping()")
#         msg = hello_world_client.sayHello()
#         print(msg)
#         msg = hello_world_client.sayMsg(HELLO_WORLD)
#         print(msg)
#
#         printer_client.printMsg('fsadfsafsaffsadfsafsafasfasf')
#
#         transport.close()
#     except Thrift.TException as tx:
#         print("%s" % (tx.message))


import thriftpy2
#from thriftpy2.rpc import client_context
from thriftpy2.rpc import make_client
# 读入thrift文件，module_name最好与server端保持一致，也可以不保持一致
service_thrift = thriftpy2.load("service.thrift", module_name="service_thrift")

client = make_client(service_thrift.HelloWorld, '127.0.0.1', 30303)
print(client.ping())
print(client.sayHello())
print(client.sayMsg('fsadfafsafsaf'))

