# -*- coding: utf-8 -*-
# @author: Spark
# @file: helloworld.thrift.py
# @ide: PyCharm
# @time: 2020-06-17 17:32:33

const string HELLO_WORLD = "world"

service HelloWorld {
    void ping(),
    string sayHello(),
    string sayMsg(1:string msg)
}

service Printer {
    void printMsg(1:string msg)
}