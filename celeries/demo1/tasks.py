# -*- coding: utf-8 -*-
# @author: Spark
# @file: tasks.py
# @ide: PyCharm
# @time: 2019-11-12 19:59:00

from celery import Celery

app = Celery()
app.config_from_object("celery_config")


@app.task
def add(x, y):
    return x + y

