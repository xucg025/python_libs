# -*- coding: utf-8 -*-
# @author: Spark
# @file: tasks.py
# @ide: PyCharm
# @time: 2020-01-07 14:05:35

import time
from celery import Celery
from celery.utils.log import get_task_logger
from celery import Task

broker = 'redis://root:ajmd123@192.168.174.28:6379/1'
backend = 'redis://root:ajmd123@192.168.174.28:6379/0'
# backend = None

app = Celery('tasks', backend=backend, broker=broker)
app.config_from_object('celery_config')


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('task done: {0}'.format(retval))
        return super(MyTask, self).on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print('task fail, reason: {0}'.format(exc))
        return super(MyTask, self).on_failure(exc, task_id, args, kwargs, einfo)


@app.task(base=MyTask)
def add(x, y):
    time.sleep(5)
    return x + y


@app.task(bind=True)
def test_mes(self):
    for i in range(1, 20):
        time.sleep(1)
        self.update_state(state="PROGRESS", meta={'p': i*10})
    return 'finish'


@app.task(bind=True)
def period_task(self):
    print('period task done: {0}'.format(self.request.id))


# app.config_from_object('celery_config')
#
#
# @app.task(bind=True)
# def period_task(self):
#     i = 0
#     while True:
#         i += 1
#         time.sleep(1)
#         print(i)
#         if i >= 30:
#             break
#     print('period task done: {0}'.format(self.request.id))
