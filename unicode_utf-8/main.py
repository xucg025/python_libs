# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-04 17:44:11

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8').decode('utf-8'))


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        h = hash(self.name)
        print(h)
        return h
    #
    # def __cmp__(self, other):
    #     return True

    def __eq__(self, other):
        return True


if __name__ == '__main__':
    p1 = Person('zhangsan', 18)
    p2 = Person('zhangsan', 18)

    s = set()
    s.add(p1)
    s.add(p2)
    print(s)