# -*- coding: utf-8 -*-
# @author: Spark
# @file: client2.py
# @ide: PyCharm
# @time: 2020-12-23 16:41:49

import thriftpy2
#from thriftpy2.rpc import client_context
from thriftpy2.rpc import make_client
# 读入thrift文件，module_name最好与server端保持一致，也可以不保持一致
service = thriftpy2.load("thrift/ip_fetcher.thrift", module_name="service_thrift")

client = make_client(service.IpFetcher, '192.168.174.30', 8089)
print(client.fetch_ip(3, 'web_task'))