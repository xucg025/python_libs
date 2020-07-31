# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2019-12-24 11:04:07

from twisted.internet import reactor, defer


class Getter:
    def getData(self, x):
         # this won't block
        d = defer.Deferred()
        reactor.callLater(2, d.callback, x * 3)
        return d



def printData(d):
    print(d)


if __name__ == '__main__':
    g = Getter()
    d = g.getData(3)
    d.addCallback(printData)

    reactor.callLater(4, reactor.stop)
    reactor.run()
