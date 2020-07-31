# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-04 09:54:14
import json, time, requests

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


def ajax_return(status=0, msg='', data=None, code=None):
    result = {
        'status': status,
        'msg': msg,
        'data': data,
        'code': code,
    }
    return jsonify(result)


#  获取post参数
def get_params():
    data = request.get_data()
    j_data = json.loads(data)
    return j_data


@app.route('/locker/index', methods=['POST', 'GET'])
def index():
    start_time = time.time()
    print(start_time)
    try:
        requests.get('http://www.google.com')
    except Exception as e:
        print('dddddddddddd')
    return ajax_return(data=start_time)


if __name__ == '__main__':
    app.run(debug=True, port=9527)
