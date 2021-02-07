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
textFile = sc.textFile("words")
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

list = ['hadoop', 'spark', 'hive', 'flume', 'kafka', 'spark', 'kafka']
rdd = sc.parallelize(list)
# rdd.cache()
# rdd.groupByKey()
# print(rdd.count())
print(rdd.collect())
pairRdd = rdd.map(lambda word: (word, 1))
print(pairRdd.collect())
pairRdd.reduceByKey(lambda a, b: a+b).foreach(print)
pairRdd.groupByKey().foreach(print)
pairRdd.keys().foreach(print)
pairRdd.values().foreach(print)
pairRdd.sortByKey().foreach(print)
pairRdd.mapValues(lambda x: x+1).foreach(print)

pairRDD1 = sc.parallelize([('spark',1),('spark',2),('hadoop',3),('hadoop',5)])
pairRDD2 = sc.parallelize([('spark','fast')])
pairRDD1.join(pairRDD2)
pairRDD1.join(pairRDD2).foreach(print)
