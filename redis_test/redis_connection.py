#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import pandas as pd
from quant_backend.settings.settings import MATCHCREDIS

r = redis.Redis(host='127.0.0.1', port=6379, db=7, password='123456')

# print(r.hgetall(name='stkRealTimeState:\x01\x01_14901'))
# r.hset(name='stkRealTimeState:{}_14901'.format('000001'), key='pe', value='1')

# redis不支持dataframe，需要将dict转化就可以存入redis,但是存进去是压缩的二进制
df = pd.DataFrame({'li':['ke', 'wei'],})
r.hset(name='stkRealTimeState:{}_14901'.format('000001'), key='pe', value=df.to_msgpack(compress='zlib'))

result = r.hget(name='stkRealTimeState:{}_14901'.format('000001'), key='pe')
# print(pd.read_msgpack(result))
# result = float(result)
# print(result)

# 可以用解析的形式进行redis连接池的连接
redis_store = redis.ConnectionPool(**MATCHCREDIS)
redisMangers = redis.StrictRedis(connection_pool=redis_store)
ss = redisMangers.hget(name='rank:office:datb:1530782325975681',key='100')
print(ss)
