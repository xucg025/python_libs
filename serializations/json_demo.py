# -*- coding: utf-8 -*-
# @author: Spark
# @file: json_demo.py
# @ide: PyCharm
# @time: 2020-06-16 09:23:29
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


if __name__ == '__main__':
    s = Student('zhangsan', 18, 90)
    dumped_s = json.dumps(s, default=lambda x: x.__dict__)
    print(dumped_s)
    sss = json.loads(dumped_s)
    print(sss)