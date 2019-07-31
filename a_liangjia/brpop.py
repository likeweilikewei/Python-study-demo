#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import time
from retry import retry
from quant_backend.util.redisManager import *



class Brpop:
    """
    模拟brpop阻塞式读取redis list内容，从而实现事件驱动
    """
    # @retry()
    def __init__(self):
        self.redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=8, password='123456')
        self.redis_manager = redis.StrictRedis(connection_pool=self.redis_pool)
        self.redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 8}
        self.local = {'host': '192.168.60.247', 'port': 6379, 'db': 0}
        self.redis_quant = RedisManager(self.local)
        self.redis_pools = redis.ConnectionPool(host='192.168.60.247', port=6379, db=1)
        self.ycf = redis.StrictRedis(connection_pool=self.redis_pools)

    def poptime_push(self):
        codes = []
        for i in range(3500):
            if i // 10 < 1:
                codes.append('stkRealTimeState:00000{}_14901'.format(i))
            elif i // 100 < 1:
                codes.append('stkRealTimeState:0000{}_14901'.format(i))
            elif i // 1000 < 1:
                codes.append('stkRealTimeState:000{}_14901'.format(i))
            elif i // 10000 < 1:
                codes.append('stkRealTimeState:00{}_14901'.format(i))
        self.redis_quant.rpush('queue_test', codes)

    def poptime_pop(self):
        time_start = time.time()
        while True:
            # self.redis_quant.brpop(keys='queue_test')
            self.redis_quant.brpop(keys='queue')
            times = time.time() - time_start
            # print('--------------------pop time--------------------')
            print(times)

    def poptime(self):
        # self.poptime_push()
        self.poptime_pop()

    def produce(self):
        for i in range(100):
            self.redis_manager.rpush('queue_test', )
            self.redis_manager.hmset('realTime:', {i:'likewei'})

    def custom_new(self):
        start_time = time.time()
        while True:
            pipe = self.ycf.pipeline()
            while True:
                count = self.ycf.llen(name='queue')
                print(count)
                for i in range(count + 50):
                    pipe.brpop(keys='queue')
                result = pipe.execute()
                print(result)
                # print('--------------time------------------')
                print(time.time() - start_time)
                break

    @retry(delay=0.1)
    def custom(self):
        start_time = time.time()
        # time_list = []
        # time_lists = []
        count = 0
        pipe = self.ycf.pipeline()
        while True:
            while True:
                if count % 1000 == 0 and count:
                    # test = self.ycf.lpop(name='queue')
                    # if not test:
                        result = pipe.execute()
                        print(result)
                        print(len(result))
                        print(time.time() - start_time)
                        count = 0
                        break
                count += 1
                pipe.brpop(keys='queue')
                # print(result)
                # print(type(result))
                # print(result.__dict__)
                # exit(0)
                # print('***')
                # print(result)
                # if not result:
                #
                #     print(2)
                #     pipe.execute()
                #     print(time.time() - start_time)
                #     break
            # start_time = time.time()
            # print(result)
            # if result:
            #     time_list.append(time.time())
            # print('\n\n------------------brpop result------------------')
            # print(str(result[1], encoding='utf-8'))
            # key = str(result[1], encoding='utf-8')
            # hash_result = self.redis_quant.hmget(name=key, keys=['dt', 'price','shrCd'])
            # print('--------------------hash result-------------------')
            # print(hash_result)
            # print('--------------------time----------------------------')
            #
            # print(time.time() - start_time)

    def pop(self):
        time1 = time.time()
        pipe = self.ycf.pipeline()
        for i in range(3000):
            pipe.brpop(keys='queue')
        pipe.execute()
        time2 = time.time()
        print('-----------time------------')
        print(time2-time1)

    def producer(self):
        self.produce()

    def customer(self):
        self.custom()
        # self.custom_new()
        # self.pop()

    def brpop(self):
        # self.producer()
        self.customer()

if __name__ == '__main__':
    brpop = Brpop()
    brpop.brpop()
    # brpop.poptime()
