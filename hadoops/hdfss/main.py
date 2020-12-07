# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-05-28 15:25:01

import pyhdfs


client = pyhdfs.HdfsClient(hosts="192.168.174.30,9000", user_name="hadoop")
print(client.get_home_directory())
print(client.get_active_namenode())
client.mkdirs('/user/hadoop')
# 从本地上传文件至集群之前，集群的目录
print("Before copy_from_local")
print(client.listdir("/user/hadoop"))

# 从本地上传文件至集群
client.copy_from_local("test.mp4", "/user/hadoop/test.mp4")

# 从本地上传文件至集群之后，集群的目录
print("After copy_from_local")
print(client.listdir("/user/hadoop"))

print(client.exists("/user/hadoop/test.mp4"))
print(client.get_content_summary("/user/hadoop"))
print(client.get_file_checksum("/user/hadoop/test.mp4"))
print(client.list_status("/user/hadoop"))
print(client.list_status("/user/hadoop/test.mp4"))


# client.copy_from_local("test.mp4", "/test/test.mp4")

from hdfs import InsecureClient
import time

# client = InsecureClient('http://192.168.174.30:50070/', user='hadoop', root='/')
# print("hdfs中的目录为:", client.list(hdfs_path="/", status=True))
# # print(client.status(hdfs_path="2020-12/2020-12-04-11.1607052949399.log.tmp", strict=True))
# # print("根目录下的文件数量为:", client.checksum(hdfs_path="2020-12/2020-12-04-11.1607052949399.log.tmp"))
# client.makedirs('hdfs_test')
# # client.write('hdfs_test/1.log', time.asctime(time.localtime(time.time())) + '\n', True)
# client.upload('a.mp4', 'test.mp4')
# # # from hdfs.client import Client
# #
# # client = Client("http://192.168.174.28:9870", root="/")
# #
# # file_path = "/aa/hadoop.env"
# # with client.read(file_path) as fs:
# #     content = fs.read()
# #     print(content)
#
# import pyhdfs
# client = pyhdfs.HdfsClient('192.168.174.30:50070', user_name='root', timeout=10)
# print(client.listdir('/'))
# print(client.get_active_namenode())
# print(client.get_home_directory())
# file_path = "/aa/hadoop.env"
# response = client.open(file_path)
# print(response.read())
#
# # 从本地上传文件至集群之前，集群的目录
# print("Before copy_from_local")
# print(client.listdir("/aa"))
#
# # 从本地上传文件至集群
# client.copy_from_local("test.mp4", "/aa/test1.mp4")
#
# # 从本地上传文件至集群之后，集群的目录
# print("After copy_from_local")
# print(client.listdir("/aa/"))
#
# print(client.exists("/user/hadoop/test.csv"))