# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-08 11:20:44


# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:
from hello import application

# 创建一个服务器，IP地址为空，8089，处理函数是application:
httpd = make_server('', 8089, application)
print('Serving HTTP on port 8089...')
# 开始监听HTTP请求:
httpd.serve_forever()