# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-05-28 15:25:01

# from hdfs.client import Client
#
# client = Client("http://192.168.174.28:9870", root="/")
#
# file_path = "/aa/hadoop.env"
# with client.read(file_path) as fs:
#     content = fs.read()
#     print(content)

import pyhdfs
client = pyhdfs.HdfsClient('192.168.174.28:9870', user_name='root', timeout=10)
print(client.listdir('/'))
print(client.get_active_namenode())
print(client.get_home_directory())
file_path = "/aa/hadoop.env"
response = client.open(file_path)
print(response.read())

# 从本地上传文件至集群之前，集群的目录
print("Before copy_from_local")
print(client.listdir("/aa"))

# 从本地上传文件至集群
client.copy_from_local("test.mp4", "/aa/test1.mp4")

# 从本地上传文件至集群之后，集群的目录
print("After copy_from_local")
print(client.listdir("/aa/"))

print(client.exists("/user/hadoop/test.csv"))