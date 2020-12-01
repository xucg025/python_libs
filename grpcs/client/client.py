# -*- coding: utf-8 -*-
# @author: Spark
# @file: client.py
# @ide: PyCharm
# @time: 2020-10-27 17:40:45


import logging

import grpc

import simple_pb2
import simple_pb2_grpc


def run():
    # 注意(gRPC Python Team): .close()方法在channel上是可用的。
    # 并且应该在with语句不符合代码需求的情况下使用。
    with grpc.insecure_channel('localhost:8028') as channel:
        stub = simple_pb2_grpc.WaiterStub(channel)
        response = stub.DoMD5(simple_pb2.Req(jsonStr='test123'))
    print("Waiter client received: {}".format(response.backJson))


if __name__ == '__main__':
    logging.basicConfig()
    run()
