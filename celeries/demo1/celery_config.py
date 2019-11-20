# -*- coding: utf-8 -*-
# @author: Spark
# @file: celery_config.py
# @ide: PyCharm
# @time: 2019-11-13 13:53:35


from kombu import Exchange,Queue

BROKER_URL = "amqp://root:ajmd123@192.168.174.28:5672//"
CELERY_RESULT_BACKEND = 'redis://root:ajmd123@192.168.174.28:6379/0' # 把任务结果存在了Redis
#
# CELERY_QUEUES = (
# Queue("default",Exchange("default"),routing_key="default"),
# Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
# Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B")
# )
# # 路由
# CELERY_ROUTES = {
# 'tasks.taskA':{"queue":"for_task_A","routing_key":"for_task_A"},
# 'tasks.taskB':{"queue":"for_task_B","routing_key":"for_task_B"}
# }
