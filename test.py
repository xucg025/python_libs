# -*- coding: utf-8 -*-
# @author: Spark
# @file: test.py
# @ide: PyCharm
# @time: 2020-12-23 09:09:38
import os

class Student(object):
      def __init__(self):
            pass

      def __getitem__(self, k):
            pass

      def __getattr__(self, item):
            pass


if __name__ == '__main__':
    s = Student()
    s.a
    print(s['ddd'])