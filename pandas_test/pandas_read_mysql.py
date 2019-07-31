#! /user/bin/env python
# -*- coding=utf-8 -*-


import sys

import redis

sys.path.append('../../')
import pandas as pd
from datetime import datetime
from old_file.settings import engine
from old_file.settings import f4

now = datetime.now()
trade_days = pd.read_sql(
    "select trade_days from calendar where exchange='SSE' and trade_days < '{}' order by trade_days ".format(
        f4(now)), engine)
max_date = f4(trade_days['trade_days'].values[-1])
gn = pd.read_sql(
    'select code,  gn_code from conseption where list_date <="{}" and delist_date >="{}"'.format(max_date,
                                                                                                 max_date),
    engine)
# for gn_code, row in gn.groupby('gn_code'):
#     # print('gn_code:', gn_code, type(gn_code))
#     # print('row:', row, type(gn_code))
#     print(row['gn_code'], '\n')
#     print(row['gn_code'].values)

# for x in gn.groupby('gn_code'):
#     print('x:', x, type(x))


"""用pandas读取mysql，并用hash插入redis"""
r = redis.ConnectionPool(host='127.0.0.1', port=6379, db=7, password='123456')
redisManger = redis.StrictRedis(connection_pool=r)
pipe = redisManger.pipeline()

_bai_ke = pd.read_sql("SELECT term, content FROM bai_ke_data", engine)
# print('bai_ke: {}'.format(_bai_ke), 'bai_ke type: {}'.format(type(_bai_ke)))
for _, bai_ke in _bai_ke.iterrows():
    print('name: {}, bai_ke: {}'.format(bai_ke['term'], bai_ke['content'].strip()))
    # print("type of baike: {}".format(type(bai_ke)))
    # print('baike: {}'.format(bai_ke))
    pipe.hset(name='indicators_teach', key=bai_ke['term'], value=bai_ke['content'].strip())
pipe.execute()
