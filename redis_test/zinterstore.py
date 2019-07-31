#! /user/bin/env python
# -*- coding=utf-8 -*-

from RedisManager import *


def zinterstore():
    """
    zinterstore不会自动创建zset key,而且只有两个集合有交集的时候才会插入，并且将两个的score相加
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 7}
    __redis_manager = RedisManager(redis_setting)
    # __redis_manager.zadd(name='likewei:one', value='math', score=1)
    # __redis_manager.zadd(name='likewei:two', value='math', score=2)
    # __redis_manager.zadd(name='likewei:three', value='math', score=3)
    # __redis_manager.zadd(name='likewei:one', value='history', score=1)
    # __redis_manager.zadd(name='likewei:two', value='history', score=2)
    # __redis_manager.zadd(name='likewei:three', value='history', score=3)

    block_set = 'tmps'
    block = 'likewei:one'
    __redis_manager.zinterstore(block_set, (block, block))
zinterstore()
