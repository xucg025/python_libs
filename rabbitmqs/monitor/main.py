# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2021-01-04 09:30:17

import pika
import csv
import os
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


class RabbitMQ:
    def __init__(self, host, user, pwd, vhost):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.vhost = vhost

    def __GetConnect(self):
        """
        得到连接信息
        返回: connection.channel()
        """
        credentials = pika.credentials.PlainCredentials(self.user, self.pwd)
        pika_conn_params = pika.ConnectionParameters(self.host, 5672, self.vhost, credentials)
        connection = pika.BlockingConnection(pika_conn_params)
        self.channel = connection.channel()

        if not self.channel:
            raise (NameError, "连接rabbitmq失败")
        else:
            return self.channel

    def ExecQuery(self):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
        调用示例：
        """

        # from pyrabbit.api import Client
        # cl = Client('192.168.174.30:5672', 'xucg', 'ajmd123')
        # aaa = cl.get_messages('vhost_test', 'queue-fanout-test-1')[0]['message_count']
        # return aaa

        channel = self.__GetConnect()
        test_1_queue = channel.queue_declare(queue="queue-fanout-test-1")
        queue_st = "test_1_queue:{0}".format(test_1_queue.method.message_count)
        # agent_queue = channel.queue_declare(queue="DTrms.AgentQueue", durable=True, exclusive=False, auto_delete=False)
        # consumer_queue = channel.queue_declare(queue="DTrms.ConsumerQueue", durable=True, exclusive=False,
        #                                        auto_delete=False, arguments={'x-max-priority': 3})
        # event_queue = channel.queue_declare(queue="DTrms.EventConsumerQueue", durable=True, exclusive=False,
        #                                     auto_delete=False)
        # queue_st = "agent_queue:{0},consumer_queue:{1},event_queue:{2}".format(agent_queue.method.message_count,
        #                                                                        consumer_queue.method.message_count,
        #                                                                        event_queue.method.message_count)

        print(queue_st)
        return queue_st

    def ToCVSFile(self, cvsFilename, dblist):
        """
        save to cvs documents
        """
        with open(cvsFilename, 'a', encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            # writer.writerow(line)


def quiryDbJob():
    print('Tick! The time is: %s' % datetime.datetime.now())
    ramq = RabbitMQ(host='192.168.174.30', user="xucg", pwd="ajmd123", vhost="vhost_test")
    resList = ramq.ExecQuery()
    ramq.ToCVSFile("queueSt.csv", resList)


def main():
    scheduler = BlockingScheduler()
    scheduler.add_job(quiryDbJob, 'interval', seconds=5)
    print('Press--- Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        scheduler.start()
    except KeyboardInterrupt as SystemExit:
        scheduler.shutdown()


if __name__ == '__main__':
    main()
