# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-12 10:14:07


class MyList(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return MyListIterator(self.num)


class MyListIterator(object):
    def __init__(self, data):
        self.data = data
        self.now = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.now < self.data:
            self.now += 1
            return self.now - 1
        raise StopIteration


from collections import Iterable, Iterator

aa = iter([123, 234])
print(dir(aa))
print(help(aa))
my_list = MyList(5)
my_list_iterator = iter(my_list)

# print(isinstance(my_list, Iterable))
# print(isinstance(my_list_iterator, Iterator))

# for i in my_list_iterator:
#     print(i)

for i in my_list:
    print(i)

