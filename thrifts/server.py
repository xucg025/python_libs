# -*- coding: utf-8 -*-
# @author: Spark
# @file: server_hello_world.py
# @ide: PyCharm
# @time: 2020-06-17 17:33:55

# import sys
# sys.path.append('./gen-py')
#
# from service import HelloWorld, Printer
# from service.ttypes import *
#
# from thrift.transport import TSocket
# from thrift.transport import TTransport
# from thrift.protocol import TBinaryProtocol
# from thrift.server import TServer
# from thrift.TMultiplexedProcessor import TMultiplexedProcessor
# import socket

import thriftpy2
from thriftpy2.rpc import make_server
service_thrift = thriftpy2.load("service.thrift", module_name="service_thrift")
import socket


class HelloWorldHandler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print("ping()")

    def sayHello(self):
        print("sayHello()")
        return "say hello from " + socket.gethostbyname(socket.gethostname())

    def sayMsg(self, msg):
        print("sayMsg(" + msg + ")")
        return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())


class PrinterHandler:
    def __init__(self):
        pass

    def printMsg(self, msg):
        print("printMsg(" + msg + ")")
        return


# hello_world_handler = HelloWorldHandler()
# printer_handler = PrinterHandler()
# hello_world_processor = HelloWorld.Processor(hello_world_handler)
# printer_processor = Printer.Processor(printer_handler)
#
# transport = TSocket.TServerSocket('127.0.0.1', 30303)
# tfactory = TTransport.TBufferedTransportFactory()
# pfactory = TBinaryProtocol.TBinaryProtocolFactory()
#
# # 多 processor
# processor = TMultiplexedProcessor()
# processor.registerProcessor('hello_world', hello_world_processor)
# processor.registerProcessor('printer', printer_processor)
#
# server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
#
# print("Starting python server...")
# server.serve()
# print("done!")

server = make_server(service_thrift.HelloWorld, HelloWorldHandler(), '127.0.0.1', 30303)
print("serving...")
server.serve()

