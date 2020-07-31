# -*- coding: utf-8 -*-
# @author: Spark
# @file: redis_lock.py
# @ide: PyCharm
# @time: 2020-06-04 11:31:45
import time
from redlock import RedLock
from functools import wraps


class RedisLockAction(object):
    def __init__(self, *args, **kwargs):
        self.redis = args

    def __call__(self, func):
        '''
        使用redis分布式锁控制action流程
        :param func:
        :return:
        '''
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                lock_key = args[0].lock_key
                redis_lock = RedLock(lock_key, self.redis, ttl=120000)
                while True:
                    acquired = redis_lock.acquire()
                    if not acquired:
                        time.sleep(1)
                        continue
                    print('redis lock acquired')
                    try:
                        func(*args, **kwargs)
                    except Exception as e:
                        print(e)
                    finally:
                        redis_lock.release()
                        print('redis lock released')
                        return
            except Exception as e:
                func(*args, **kwargs)
        return wrapper
