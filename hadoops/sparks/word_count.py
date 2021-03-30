# -*- coding: utf-8 -*-
# @author: Spark
# @file: word_count.py
# @ide: PyCharm
# @time: 2021-01-07 14:14:48

import os, sys
from pyspark import SparkConf, SparkContext
os.environ['SPARK_HOME'] = "D:\\bd\\spark-3.0.0-preview2-bin-hadoop2.7"
sys.path.append("D:\\bd\\spark-3.0.0-preview2-bin-hadoop2.7\\python")
sys.path.append("D:\\bd\\spark-3.0.0-preview2-bin-hadoop2.7\\python\\lib\\py4j-0.9-src.zip")

conf = SparkConf().setMaster('local').setAppName('word_count')
sc = SparkContext(conf=conf)
lines = sc.textFile("words")
print(lines.count())
rdd = lines.map(lambda x: x.split(' '))
# print(rdd.collect())
rdd.foreach(print)
print(rdd.count())
rdd1 = lines.flatMap(lambda x: x.split(' '))
# rdd1.foreach(print)
print(rdd1.count())

rdd2 = rdd1.filter(lambda x: len(x) > 3)
# rdd2.foreach(print)
print(rdd2.count())

# rdd3 = rdd2.reduce(lambda x, y: x+y)
# print(rdd3)

rdd4 = rdd1.map(lambda x: (x, 1))
rdd5 = rdd4.reduceByKey(lambda x, y: x + y)
print(rdd5.collect())
rdd5.keys().foreach(print)
rdd5.values().foreach(print)
rdd5.sortByKey().foreach(print)
rdd5.sortBy(lambda x: x[1], False).foreach(print)
rdd5_1 = rdd5.mapValues(lambda x: x*10).sortBy(lambda x: x[1])
rdd5_1.saveAsTextFile('words_3')

print(rdd1.countByValue())

rdd6 = rdd4.groupByKey()
# rdd6.cache()
print(rdd6.collect())
print(rdd6.count())

rdd6.map(lambda x: (x[0], sum(x[1]))).foreach(print)

# print(textFile.first())
# textFile.saveAsTextFile('words_2')
# wordCount = textFile.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b : a + b)
# print(wordCount.count())
# print(wordCount.first())
# # print(wordCount.collect())
# print(wordCount.take(5))
# wordCount.foreach(print)

# dd = textFile.map(lambda line: len(line.split(" "))).reduce(lambda a, b: a+b)
# print(dd)

# words = ['hadoop', 'spark', 'hive', 'flume', 'kafka', 'spark', 'kafka', 'hbase', 'zookeeper']
# rdd = sc.parallelize(words)
# rdd1 = rdd.map(lambda x: (x, 1))
# rdd2 = rdd1.reduceByKey(lambda x, y: x+y)
# print(rdd2.collect())
# rdd = sc.parallelize(list)
# rdd.foreach(print)
# # rdd.cache()
# # rdd.groupByKey()
# # print(rdd.count())
# print(rdd.collect())
# pairRdd = rdd.map(lambda word: (word, 1))
# print(pairRdd.collect())
# pairRdd.reduceByKey(lambda a, b: a+b).foreach(print)
# pairRdd.groupByKey().foreach(print)
# pairRdd.keys().foreach(print)
# pairRdd.values().foreach(print)
# pairRdd.sortByKey().foreach(print)
# pairRdd.mapValues(lambda x: x+1).foreach(print)
#
# pairRDD1 = sc.parallelize([('spark',1),('spark',2),('hadoop',3),('hadoop',5)])
# pairRDD2 = sc.parallelize([('spark','fast')])
# pairRDD1.join(pairRDD2)
# pairRDD1.join(pairRDD2).foreach(print)
