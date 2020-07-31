# -*- coding: utf-8 -*-
# @author: Spark
# @file: main.py
# @ide: PyCharm
# @time: 2020-05-14 09:32:59

import time
import redis

# client = redis.StrictRedis()


# def is_action_allowed(user_id, action_key, period, max_count):
#     key = 'hist:%s:%s' % (user_id, action_key)
#     now_ts = int(time.time() * 1000)  #
#     with client.pipeline() as pipe:  # client  StrictRedis
#         pipe.zadd(key, now_ts, now_ts)  # value  score
#         pipe.zremrangebyscore(key, 0, now_ts - period * 1000)
#         pipe.zcard(key)
#         pipe.expire(key, period + 1)
#         _, _, current_count, _ = pipe.execute()
#     return current_count <= max_count
#
#
# for i in range(100):
#     print(is_action_allowed("laoqian", "reply", 60, 5))


class Funnel(object):
    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity  #
        self.leaking_rate = leaking_rate  #
        self.left_quota = capacity  #
        self.leaking_ts = time.time()  #

    def make_space(self):
        now_ts = time.time()
        delta_ts = now_ts - self.leaking_ts  #
        delta_quota = delta_ts * self.leaking_rate  #
        if delta_quota < 1:  #
            return
        self.left_quota += delta_quota  #
        self.leaking_ts = now_ts  #
        if self.left_quota > self.capacity:  #
            self.left_quota = self.capacity

    def watering(self, quota):
        self.make_space()
        if self.left_quota >= quota:  #
            self.left_quota -= quota
            return True
        return False


funnels = {}  #


def is_action_allowed(user_id, action_key, capacity, leaking_rate):
    key = '%s:%s' % (user_id, action_key)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)


for i in range(10000):
    allowed = is_action_allowed('laoqian', 'reply', 200, 500)
    if allowed:
        continue
    else:
        print(allowed)
        time.sleep(.01)
        allowed = is_action_allowed('laoqian', 'reply', 200, 500)
        print(allowed)


    # print(is_action_allowed('laoqian', 'reply', 200, 500))
    # time.sleep(.0000001)
