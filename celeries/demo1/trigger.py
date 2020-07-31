# -*- coding: utf-8 -*-
# @author: Spark
# @file: trigger.py
# @ide: PyCharm
# @time: 2020-01-07 14:12:47


from tasks import test_mes, add
import sys, time


def pm(body):
    res = body.get('result')
    if body.get('status') == 'PROGRESS':
        sys.stdout.write('\r任务进度: {0}%'.format(res.get('p')))
        sys.stdout.flush()
    else:
        print('\r')
        print(res)


for i in range(2):
    r = test_mes.delay()
    print(r.get(on_message=pm, propagate=False))


# for i in range(10):
#     result = add.delay(i, i+1)
#     while not result.ready():
#         print(time.time())
#         time.sleep(1)
#     print('result--->{}'.format(result.get()))
#     # result.get(propagate=False)
#     # print(result)
#     # print(result.get())