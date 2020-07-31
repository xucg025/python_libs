# -*- coding: utf-8 -*-
# @author: Spark
# @file: gun.py
# @ide: PyCharm
# @time: 2020-06-04 11:44:01

# import os
# import gevent.monkey
# gevent.monkey.patch_all()
# import multiprocessing
#
# # 服务地址（adderes:port）
# bind = '0.0.0.0:9527'
# # 启动进程数量
# workers = multiprocessing.cpu_count() * 2 +1
# worker_class = 'gevent'
# # threads = 20
# preload_app = True
# reload = True
# x_forwarded_for_header = 'X_FORWARDED-FOR'

import gevent.monkey

gevent.monkey.patch_all()

import multiprocessing
import os

if not os.path.exists('log'):
    os.mkdir('log')

# debug = True
# loglevel = 'debug'
bind = '0.0.0.0:9527'
pidfile = 'log/gunicorn.pid'
# logfile = 'log/debug.log'
# errorlog = 'log/error.log'
# accesslog = 'log/access.log'

# 启动的进程数
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'

x_forwarded_for_header = 'X-FORWARDED-FOR'
