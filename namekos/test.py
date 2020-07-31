# -*- coding: utf-8 -*-
# @author: Spark
# @file: test.py
# @ide: PyCharm
# @time: 2020-05-11 14:23:56

from flask import Flask, request
# from flasgger import Swagger
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)

CONFIG = {'AMQP_URI': "amqp://guest:guest@192.168.174.28"}


@app.route('/hello', methods=['POST', 'GET'])
def hello():
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.greeting_service.hello(name="jerry")
        return result, 200


app.run(debug=True, port=8083)
