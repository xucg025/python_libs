# -*- coding: utf-8 -*-
# @author: Spark
# @file: main_1.py
# @ide: PyCharm
# @time: 2019-12-24 11:21:16

from twisted.internet import protocol, reactor, defer, utils
from twisted.protocols import basic


class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, user):
        self.factory.getUser(user).addErrback(lambda _: "Internal error in server")\
            .addCallback(lambda m: (self.transport.write(str(m) + "/r/n"), self.transport.loseConnection()))


class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

    def getUser(self, user):
        return utils.getProcessOutput("finger", [user])


if __name__ == '__main__':
    reactor.listenTCP(1079, FingerFactory())
    reactor.run()
