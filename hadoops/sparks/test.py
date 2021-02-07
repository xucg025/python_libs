# -*- coding: utf-8 -*-
# @author: Spark
# @file: test.py
# @ide: PyCharm
# @time: 2021-01-07 10:36:30

import os, sys
from pyspark import SparkConf, SparkContext
os.environ['SPARK_HOME'] = "D:\\bd\\spark-3.0.0-preview2-bin-hadoop2.7"

# You might need to enter your local IP
# os.environ['SPARK_LOCAL_IP']="192.168.2.138"

# Path for pyspark and py4j
sys.path.append("D:\\bd\\spark-3.0.0-preview2-bin-hadoop2.7\\python")
sys.path.append("D:\\bd\\spark-3.0.0-preview2-bin-hadoop2.7\\python\\lib\\py4j-0.9-src.zip")

conf = SparkConf().setMaster('local').setAppName('word_count')
sc = SparkContext(conf=conf)
d = ['a b c d', 'b c d e', 'c d e f']
d_rdd = sc.parallelize(d)
rdd_res = d_rdd.flatMap(lambda x: x.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
print(rdd_res.collect())
