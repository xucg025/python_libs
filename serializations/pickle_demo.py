# -*- coding: utf-8 -*-
# @author: Spark
# @file: pickle_demo.py
# @ide: PyCharm
# @time: 2020-06-16 09:23:38

import pickle


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


if __name__ == '__main__':
    s = Student('zhangsan', 18, 90)
    dumped_s = pickle.dumps(s)
    print(dumped_s)
    sss = pickle.loads(dumped_s)
    print(sss)