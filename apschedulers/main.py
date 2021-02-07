# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2019-12-26 15:56:47

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import datetime
import logging, time

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log1.txt',
                    filemode='a')


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def date_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
    print(1/0)


def my_listener(event):
    if event.exception:
        print('任务出错了！！！！！！')
    else:
        print('任务照常运行...')

# print(datetime.datetime.now() + datetime.timedelta(seconds=5))
# scheduler = BlockingScheduler()
scheduler = BackgroundScheduler()
scheduler._daemon = False
# scheduler.add_job(func=date_test, args=('一次性任务,会出错',),
#                   next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=5),
#                   id='date_task', trigger='interval', minutes=1)
# scheduler.add_job(func=date_test, args=('一次性任务,会出错',), trigger='cron',
#                   day_of_week='thu', hour=16, minute=45)
scheduler.add_job(func=aps_test, args=('循环任务_1',), trigger='interval', seconds=3, id='111', name='interval_task')
# scheduler._logger = logging

scheduler.add_job(func=aps_test, args=('循环任务_2',), trigger='interval', seconds=5, id='222', name='interval_task')

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED)
# scheduler.start()


print(scheduler.get_jobs())

print('fsdafafsafasf')




