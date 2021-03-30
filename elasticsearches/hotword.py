# -*- coding: utf-8 -*-
# @author: Spark
# @file: hotword.py
# @ide: PyCharm
# @time: 2021-02-20 16:41:35

import tornado.ioloop
import tornado.web
import os
import time

# 配置文件
conf = {"port": 9527,
        "ext_dic": "ext.dic",
        "stopwords": "stop.dic"
        }

# Server句柄


class MainHandler(tornado.web.RequestHandler):
    # 初始化，传入字典文件
    def initialize(self, file):
        self.file = file
        # 文件不存在就创建
        if not os.access(self.file, os.F_OK):
            f = open(self.file, 'w')
            f.close()
    # GET method

    def get(self):
        f = open(self.file, 'r', encoding='utf-8')
        data = f.read()
        f.close()
        self.set_header("Content-Type", "text/plain; charset=UTF-8")
        self.set_header("ETag", "2")
        self.write(data)

    # HEAD mothod
    def head(self):
        # 获取更新时间，设置为上次更改的标志
        mTime = time.strftime(
            '%Y-%m-%d %H:%M:%S',
            time.localtime(
                os.stat(
                    self.file).st_mtime))
        self.set_header("Last-Modified", mTime)
        self.set_header("ETag", "2")
        self.set_header("Content-Length", "0")
        self.finish()

# 注册webMapping


def make_app():
    return tornado.web.Application([
        (r"/extdic", MainHandler, {"file": conf["ext_dic"]}),
        (r"/stopwords", MainHandler, {"file": conf["stopwords"]})
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(conf["port"])
    tornado.ioloop.IOLoop.current().start()
