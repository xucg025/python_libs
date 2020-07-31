# -*- coding: utf-8 -*-
# @author: Spark
# @file: main2.py
# @ide: PyCharm
# @time: 2019-12-26 16:10:08

from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', hour='8-23')
def request_update_status():
    print('Doing job')

scheduler.start()