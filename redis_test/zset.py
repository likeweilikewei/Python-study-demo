#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import pandas as pd
from quant_backend.util.redisManager import RedisManager
# from quant_backend.settings.settings import redisManager3

# r = redis.Redis(host='127.0.0.1', port=6379, db=7, password='123456')

# print(r.hgetall(name='stkRealTimeState:\x01\x01_14901'))
# r.hset(name='stkRealTimeState:{}_14901'.format('000001'), key='pe', value='1')

# redis不支持dataframe，需要将dict转化就可以存入redis,但是存进去是压缩的二进制
# df = pd.DataFrame({'li':['ke', 'wei'],})
# r.hset(name='stkRealTimeState:{}_14901'.format('000001'), key='pe', value=df.to_msgpack(compress='zlib'))
#
# result = r.hget(name='stkRealTimeState:{}_14901'.format('000001'), key='pe')
# print(pd.read_msgpack(result))
# result = float(result)
# print('result:', result)
# print('decode result:', result.str.decode('utf-8'))

# # 如果后面的set没有，则不会进行任何动作，目的set有没有不要紧
# r.zinterstore('temp_codes_test', ('14904ZYJY', '14902000009'))
#
# # 取出hash结构的所有行，观察结果并转化类型为str
# results = r.hgetall(name='stkRealTimeState:000001_14901')
# print(type(result))
# print('results:', results)
# result_df = pd.DataFrame([results])
# print('result_df:', result_df)
# print('result_df type:', type(result_df))
# column_list = result_df.columns.values.tolist()
# print('column:', column_list)

# if b'wvadUpCrossZero' in column_list:
#     print("b'code' in column_list")
# else:
#     print("'b'code not in column_list")
# result_df = result_df.rename(columns={
#             b'code': 'code',
#         })
#
# result_df['code'] = result_df['code'].str.decode('utf-8')
# print('change byte to str:', result_df)

# """
# zadd StrictRedis的zadd顺序是name score value, Redis的顺序是name value score
# zrange取出指定索引区间的成员value,返回列表
# """
# r.zadd('zset_test', 'likewe', 0)
# r.zadd('zset_test', 'haogongxia', 1)
# r.zadd('zset_test', 'lieweiwei', 2)
# a = r.zrange(name='zset_test', start=0, end=-1)
# print('a:', a)


def zscore():
    """
    返回有序集中，成员的分数值
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 7}
    __redis_manager = RedisManager(redis_setting)

    result = __redis_manager.zscore(name='conception:14904WGZF', value='002869_14901')
    print(result)
# zscore()


def zcard():
    """
    获取有序集合的成员数
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 7}
    __redis_manager = RedisManager(redis_setting)

    result = __redis_manager.zcard(name='14901codes')
    print(result)
# zcard()


def zscan():
    """
    迭代有序集合中的元素（包括元素成员和元素分值）
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 0}
    __redis_manager = RedisManager(redis_setting)
    result = __redis_manager.zscan(name='14905AHS')
    print(result)
    print(len(result[1]))
# zscan()


def zscan_match():
    """
    测试带匹配模式的scan
    匹配里面的信息
    :return:
    """
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 0}
    __redis_manager = RedisManager(redis_setting)
    ss = __redis_manager.zscan_match(name='rank:office:number:1530782325975682',match='2*',count=100)
    for i in ss:
        print(i)
# zscan_match()


def zset():
    redis_setting = {'host': '192.168.60.247', 'port': 6379, 'db': 10}
    __redis_manager = RedisManager(redis_setting)
    # print(r.hgetall(name='stkRealTimeState:\x01\x01_14901'))
    __redis_manager.zadd(name='plate_index:ranking:{}'.format('industry'), value='汽车', score='3')
# zset()


def zrem():
    redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 6}
    __redis_manager = RedisManager(redis_setting)
    # __redis_manager = redis.StrictRedis(host='127.0.0.1', port=6379, password='123456', db=6)
    pipe = __redis_manager.pipeline()
    pipe.zrem('li',*['ke','wei'])
    pipe.execute()
    # __redis_manager.zrem_member(key='li',values='ke')
# zrem()

redis_setting = {'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 3}
rediss = RedisManager(redis_setting)


def del_ranking_value(name, value_list):
    """
    删除排行榜的value
    :param name: 排行榜名
    :param value_list: 值
    :return:
    """
    __pipe = rediss.pipeline()
    __pipe.zrem(name, *value_list)


def generate_ranking_name(del_names):
    """
    生成删除的排行榜的name和value
    :param del_names:删除的hash的name
    :return:
    """
    _industry = []
    _conseption = []
    _region = []
    for __name in del_names:
        __result = __name.split(':')
        print(__result)
        __new_name = __result[-1]
        __class = __result[1]
        if __class == '14903':
            _industry.append(__new_name)
        elif __class == '14904':
            _conseption.append(__new_name)
        else:
            _region.append(__new_name)
    return _industry, _conseption, _region


def del_ranking(del_names):
    """
    删除排行控制模块
    :param del_names:删除的hash name
    :return:
    """
    _industry, _conseption, _region = generate_ranking_name(del_names=del_names)
    del_ranking_value(name='plateIndex:plateRiseAndFallRate:14903', value_list=_industry)
    del_ranking_value(name='plateIndex:plateRiseAndFallRate:14904', value_list=_conseption)
    del_ranking_value(name='plateIndex:plateRiseAndFallRate:14905', value_list=_region)
# del_ranking(['plateIndex:14905:AHS'])

