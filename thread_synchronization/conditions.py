# -*- coding: utf-8 -*-
# @author: Spark
# @file: conditions.py
# @ide: PyCharm
# @time: 2020-07-01 18:05:02

import time
import threading
from threading import Condition
# condition


class XiaoMing(threading.Thread):
    def __init__(self, cond):
        self.cond = cond
        super().__init__(name="xiaoming")

    def run(self):
        # 上锁
        self.cond.acquire()
        # 线程挂起，等待被唤醒
        # 等待-释放锁；被唤醒-获取锁
        self.cond.wait()
        print('{}:ennn. '.format(self.name))
        # 唤醒等待此条件变量的一个线程
        self.cond.notify()
        # 线程挂起，等待被唤醒
        # 等待-释放锁；被唤醒-获取锁
        self.cond.wait()

        print('{}:好嗒. '.format(self.name))
        # 释放解锁
        self.cond.release()

class Teacher(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="teacher")
        self.cond = cond

    def run(self):
        # 上锁
        self.cond.acquire()
        print('{}:hello ~ xiaoming. '.format(self.name))
        # 唤醒等待此条件变量的一个线程
        self.cond.notify()
        # 线程挂起，等待被唤醒
        # 等待-释放锁；被唤醒-获取锁
        self.cond.wait()

        print('{}:我们来念一首诗吧! . '.format(self.name))
        # 唤醒等待此条件变量的一个线程
        self.cond.notify()
        # 释放解锁
        self.cond.release()

if __name__ == '__main__':
    condition = Condition()
    xiaoming = XiaoMing(condition)
    teacher = Teacher(condition)
    # 启动顺序很重要
    xiaoming.start()
    teacher.start()

