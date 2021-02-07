# -*- coding: utf-8 -*-
# @author: Spark
# @file: client.py
# @ide: PyCharm
# @time: 2020-12-23 16:29:20

import sys
import json
from service import IpFetcher
# from service.ttypes import *
# from service.constants import *
# from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('192.168.174.30', 8089)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = IpFetcher.Client(protocol)
# Connect!
transport.open()

msg = client.fetch_ip(3, 'web_pub_task')
print(msg)
transport.close()