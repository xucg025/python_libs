# -*- coding: utf-8 -*-
# @author: Spark
# @file: hello.py
# @ide: PyCharm
# @time: 2020-06-08 11:20:59


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
