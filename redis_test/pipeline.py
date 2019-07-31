#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import pandas as pd


"""
不能在pipeline中间做操作，否则取出来的都是一个个redis的查询操作
在pipe后得到的是结果的list
"""
def pipeline_test():
    r = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7, password='123456')
    redisManger = redis.StrictRedis(connection_pool=r)
    stocks = redisManger.keys('stkRealTimeState:*_14901')  # Redis Keys 命令用于查找所有符合给定模式 pattern 的 key
    print(stocks)

    pipe = redisManger.pipeline()
    # [pipe.hgetall(stock) for stock in stocks]
    lists = []
    for stock in stocks:
        li = pipe.hget(name='stkRealTimeState:000410_14901', key='pe')
        # print('result:', result)
        lists.append(li)
    result = pipe.execute()
    print('result:', result)
    print('lists:{}'.format(lists))

# pipeline_test()


def pipeline_tests():
    r = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7, password='123456')
    redisManger = redis.StrictRedis(connection_pool=r)
    # stocks = redisManger.keys('stkRealTimeState:*_14901')  # Redis Keys 命令用于查找所有符合给定模式 pattern 的 key
    # print(stocks)
    #
    pipe = redisManger.pipeline()
    # # [pipe.hgetall(stock) for stock in stocks]
    # lists = []
    # for stock in stocks:
    #     li = pipe.hget(name='stkRealTimeState:000410_14901', key='pe')
    #     # print('result:', result)
    #     lists.append(li)
    result = pipe.execute()
    print('result:', result)
    # print('lists:{}'.format(lists))
pipeline_tests()
