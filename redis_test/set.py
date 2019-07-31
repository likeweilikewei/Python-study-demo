#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import pandas as pd
# from RedisManager import *


def zinterstore():
    """
    zinterstore不会自动创建zset key,而且只有两个集合有交集的时候才会插入，并且将两个的score相加
    :return:
    当两个zset集合交并到目的集合，即使目的集合不是zset也会将目的集合变为zset，并删除原来的内容
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 8}
    __redis_manager = RedisManager(redis_setting)
    # __redis_manager.zadd(name='likewei:one', value='math', score=1)
    # __redis_manager.zadd(name='likewei:two', value='math', score=2)
    # __redis_manager.zadd(name='likewei:three', value='math', score=3)
    # __redis_manager.zadd(name='likewei:one', value='history', score=1)
    # __redis_manager.zadd(name='likewei:two', value='history', score=2)
    # __redis_manager.zadd(name='likewei:three', value='history', score=3)

    block_set = 'tmp'
    block = 'likewei:one'
    __redis_manager.zinterstore(block_set, (block, block))
# zinterstore()


def sscan():
    """
    迭代查询所有的成员
    (0, [b'b', b'a', b'c'])
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 8}
    __redis_manager = RedisManager(redis_setting)
    result = __redis_manager.sscan(name='set')
    print(result)
    for i in result[1]:
        print(i)
        print(str(i, encoding='utf-8'))
# sscan()


def smembers():
    """
    返回集合中的所有的成员。 不存在的集合 key 被视为空集合。
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 8}
    __redis_manager = RedisManager(redis_setting)
    result = __redis_manager.smembers(key='set')
    print(result)
    print(len(result))
    __redis_manager.zrem(name='tmp')
    for i in result:
        # print(i)
        i = str(i, encoding='utf-8')
        print(i)
        __redis_manager.zadd(name='tmp', score=0, value=i)
# smembers()


def zrem():
    """
    删除的时候没有name或者value都不会报错
    :return:
    """
    __pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=6, password='123456',
                                       decode_responses=True)
    __redis = redis.StrictRedis(connection_pool=__pool)
    __redis.zrem('aaa','aaaaa')
zrem()
