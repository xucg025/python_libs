# -*- coding: utf-8 -*-
# @author: Spark
# @file: lock_rlock.py
# @ide: PyCharm
# @time: 2020-07-01 17:54:48

import threading
mutex = threading.Lock() #Lock对象
mutex.acquire()
# lock.acquire()  #产生了死琐。
# lock.release()
print(mutex.locked())
mutex.release()
print(mutex.locked())

mutex.acquire()
mutex.release()

r_mutex = threading.RLock()
a = r_mutex.acquire()
b = r_mutex.acquire()
c = r_mutex.release()
d = r_mutex.release()
