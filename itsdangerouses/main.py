# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-01-07 13:14:07

from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired
import time

serializer = TimedJSONWebSignatureSerializer(secret_key='secret_key', expires_in=5)
res = serializer.dumps(obj={'test': 1024})
print(res.decode())

try:
    res = serializer.loads(res)
    print(res)
except SignatureExpired:
    print('SignatureExpired')

time.sleep(3600)
