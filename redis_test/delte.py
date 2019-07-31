#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
from quant_backend.util.redisManager import RedisManager

# r = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7, password='123456')
# redisManager = redis.StrictRedis(connection_pool=r)
# pipes = redisManager.pipeline()
# result = pipes.keys('stkRealTimeState:*')
# pipes.execute()
# print('result: {}'.format(*result))

# result = redisManager.keys(pattern='li*')
# print('result: {}'.format(redisManager.keys(pattern='li*')))
# redisManager.delete('like')
# results = redisManager.keys(pattern='li*')
# print('result: {}'.format(results))

"""生成的是一个迭代器"""
# print('test: {}'.format(result[i] for i in range(len(result))))


# key_list = redisManager.keys(name='li*')
# print('keys:{}'.format(key_list))
# redisManager.delete_by_list(key_list=key_list)
# key_list_after = redisManager.keys(name='li*')
# print('keys: {}'.format(key_list_after))


def del_keys():
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 3}
    __redis_manager = RedisManager(redis_setting)
    s =__redis_manager.keys('stkRealTimeState:*')
    print(s)
del_keys()
