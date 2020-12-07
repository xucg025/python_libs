# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-12-07 11:42:22

from mrjob.job import MRJob
import re


class MRWordCount(MRJob):
    """
    line:一行数据
        (a,1)(b,1)(c,1)
        (a,1)(c1)
        (a1)
    """
    def mapper(self, _, line):
        pattern = re.compile(r'(\W+)')
        for word in re.split(pattern=pattern, string=line):
            if word.isalpha():
                yield (word.lower(), 1)

    def reducer(self, word, count):
        """
        shuffle and sort 之后
        :param word:
        :param count:
        :return:
        """
        l = list(count)
        yield (word, sum(l))


if __name__ == '__main__':
    MRWordCount.run()  # run()方法，开始执行MapReduce任务。
