# -*- coding: utf-8 -*-
# @author: Spark
# @file: server.py
# @ide: PyCharm
# @time: 2020-12-23 16:18:13

import sys
# sys.path.append('./gen-py')

from service import IpFetcher
from service.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.TMultiplexedProcessor import TMultiplexedProcessor
import socket


class IpFetcherHandler(object):
    def __init__(self):
        pass

    def fetch_ip(self, web_id, f):
        print(web_id, f)
        return 'http://124.25.75.25:80'


if __name__ == '__main__':
    handler = IpFetcherHandler()
    processor = IpFetcher.Processor(handler)
    transport = TSocket.TServerSocket('127.0.0.1', 8007)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("Starting python server...")
    server.serve()