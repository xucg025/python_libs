# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-16 09:39:02

from functools import reduce, partial

# def multiply(a, b):
#     return a * b
#
#
# s = reduce(multiply, [1, 2, 3, 4, 5])
# print(s)

# '123456' --->  123456

# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def char2num(s):
#     return DIGITS[s]
#
# s = '123456'
# e = reduce(lambda x, y: 10*x+y, map(char2num, s))
# print(e)
#
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
#
#
# int2 = partial(int, base=10)
# print(int2('11234455'))


# import threading, time
#
# s = threading.local()
#
#
# def p():
#     time.sleep(5)
#     print(s.name)
#
#
# def f1():
#     s.name = 'func f1'
#     p()
#
#
# def f2():
#     s.name = 'func f2'
#     p()
#
#
# t1 = threading.Thread(target=f1)
# t2 = threading.Thread(target=f2)
# t1.daemon = True
# t2.daemon = True
# t1.start()
# t2.start()
# # t1.join()
# # t2.join()


class Student(object):
    def __init__(self):
        pass

    def __getattr__(self, item):
        return 111


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __setattr__(self, key, value):
        print('fsadfsafasfdasfas')
        object.__setattr__(self, key, value)

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == '__main__':
    Chain().key = 'fasdfas'
   # print(Chain().status.user.timeline.list)
