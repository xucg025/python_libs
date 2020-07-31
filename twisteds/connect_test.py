# -*- coding: utf-8 -*-
# @author: Spark
# @file: connect_test.py
# @ide: PyCharm
# @time: 2019-12-24 11:33:42


from twisted.internet import reactor, defer, protocol


class CallbackAndDisconnectProtocol(protocol.Protocol):
    # Twisted建立网络连接的固定套路
    def connectionMade(self):
        # “事件响应器”handleSuccess对此事件作出处理
        self.factory.deferred.callback("Connected!")
        self.transport.loseConnection()


class ConnectionTestFactory(protocol.ClientFactory):
    # Twisted建立网络连接的固定套路
    protocol = CallbackAndDisconnectProtocol

    def __init__(self):
        self.deferred = defer.Deferred()  # 报告发生了延迟事件，防止程序阻塞在这个任务上

    def clientConnectionFailed(self, connector, reason):
        self.deferred.errback(reason)  # “事件响应器”handleFailure对此事件作出处理


def testConnect(host, port):
    testFactory = ConnectionTestFactory()
    reactor.connectTCP(host, port, testFactory)
    return testFactory.deferred  # 返回连接任务的deferred


def handleSuccess(result, port):
    # deferred“事件响应器”：连接任务完成的处理
    print("Connected to port %i" % port)
    reactor.stop()


def handleFailure(failure, port):
    # deferred“事件响应器”：连接任务失败的处理
    print("Error connecting to port %i: %s" %
          (port, failure.getErrorMessage()))
    reactor.stop()


if __name__ == "__main__":
    import sys
    if not len(sys.argv) == 3:
        print("Usage: connectiontest.py host port")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    connecting = testConnect(host, port)
    # 调用函数，返回deferred
    connecting.addCallback(handleSuccess, port)
    # 建立deferred“事件响应器”
    connecting.addErrback(handleFailure, port)
    # 建立deferred“事件响应器”
    reactor.run()
