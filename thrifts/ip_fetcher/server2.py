# -*- coding: utf-8 -*-
# @author: Spark
# @file: server2.py
# @ide: PyCharm
# @time: 2020-12-23 16:36:02


import thriftpy2
from thriftpy2.rpc import make_server
service = thriftpy2.load("thrift/ip_fetcher.thrift", module_name="service_thrift")
import socket


class IpFetcherHandler(object):
    def __init__(self):
        pass

    def fetch_ip(self, web_id, f):
        print(web_id, f)
        return 'http://124.25.75.25:80'


server = make_server(service.IpFetcher, IpFetcherHandler(), '0.0.0.0', 8089)
print("serving...")
server.serve()