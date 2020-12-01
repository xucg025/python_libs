# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-11-25 09:59:14

from elasticsearch import Elasticsearch

es = Elasticsearch(
    ['192.168.174.30:9200'],
    # 认证信息
    # http_auth=('elastic', 'changeme')
)
# print(es.ping())
# print(es.info())
# print(es.cluster.health())
# print(es.cluster.client.info())
# print(es.cluster.stats())
#
# print(es.cat.health())
# print(es.cat.master())
# print(es.cat.nodes())
# print(es.cat.indices())
# print(es.cat.count())
# print(es.cat.plugins())
# print(es.cat.templates())

es.indices.create(index='my-index')


