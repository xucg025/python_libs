# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-06-18 13:16:29

import requests
from flask import Flask
from py_zipkin.zipkin import zipkin_span, create_http_headers_for_new_span
import time

app = Flask(__name__)

app.config.update({
    "ZIPKIN_HOST": "127.0.0.1",
    "ZIPKIN_PORT": "9411",
    "APP_PORT": 5000,
    # any other app config-y things
})


def do_stuff():
    time.sleep(2)
    headers = create_http_headers_for_new_span()
    requests.get('http://localhost:6000/service1/', headers=headers)
    return 'OK'


def http_transport(encoded_span):
    # encoding prefix explained in https://github.com/Yelp/py_zipkin#transport
    #body = b"\x0c\x00\x00\x00\x01"+encoded_span
    body = encoded_span
    zipkin_url = "http://127.0.0.1:9411/api/v1/spans"
    # zipkin_url = "http://{host}:{port}/api/v1/spans".format(
    #   host=app.config["ZIPKIN_HOST"], port=app.config["ZIPKIN_PORT"])
    headers = {"Content-Type": "application/x-thrift"}

    # You'd probably want to wrap this in a try/except in case POSTing fails
    r = requests.post(zipkin_url, data=body, headers=headers)
    print(type(encoded_span))
    print(encoded_span)
    print(body)
    print(r)
    print(r.content)


@app.route('/')
def index():
    with zipkin_span(service_name='webapp', span_name='index', transport_handler=http_transport, port=5000,
                     sample_rate=100):
        with zipkin_span(service_name='webapp', span_name='do_stuff'):
            do_stuff()
        time.sleep(1)
    return 'OK', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
