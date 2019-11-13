# -*- coding: utf-8 -*-
# @author: Spark
# @file: tasks.py
# @ide: PyCharm
# @time: 2019-11-12 19:59:00

from celery import Celery
# app = Celery('tasks', broker='amqp://root:ajmd123@192.168.174.28:5672//')

app = Celery()
app.config_from_object("celery_config")

@app.task
def add(x, y):
    return x + y

# import subprocess
# from time import sleep
#
# from celery import Celery
#
# backend = 'db+mysql://root:@10.1.2.3/celery'
# broker = 'amqp://guest@localhost//'
#
# app = Celery('tasks', broker=broker)
#
# @app.task
# def add(x, y):
#     sleep(10)
#     return x + y
# #
# # @app.task
# # def hostname():
# #     return subprocess.check_output(['hostname'])
