#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
判断是否是pandas类型
"""

import os

import pandas as pd
import time
import numpy as np
import datetime

from quant_backend.models import engine


print(os.path.dirname(__file__))
print(os.path.pardir)
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
CURRENT_PATH = os.path.join(os.path.dirname(__file__))
# 缓存
CACHE_PATH = os.path.join(CURRENT_PATH, 'cache')
print(CACHE_PATH)


def to_hdf():
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4, 4.1, 4.6], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    print('df:{}'.format(df))
    day='2017-01-01'
    day = 'quota_' + str(day).replace('-', '')
    print(day)
    df.to_hdf(os.path.join(CACHE_PATH, 'quota.h5'), day, format='table', complevel=4, complib='blosc')
# to_hdf()


def mysql_hdf(day):
	technical = day.strftime('%Y')
	valuation_df = pd.read_sql("""
        SELECT * FROM valuation_{} WHERE date = '{}'
        """.format(technical, day), engine)
	techinical_df = pd.read_sql("""
		        SELECT * FROM technical_{} WHERE date = '{}'
		        """.format(technical, day), engine)
	base_df = pd.read_sql("""
		        SELECT code,name FROM basic
		        """, engine)
	if not valuation_df.empty and not techinical_df.empty:
		for col in ['create_time', 'update_time']:
			del valuation_df[col]
			del techinical_df[col]
		for col in ['ipo_date', 'change_date']:
			del valuation_df[col]
		valuation_df = valuation_df.replace(999999999.0000, np.nan)
		df = techinical_df.merge(valuation_df, on=['code', 'date'], how='outer')
		df = df.merge(base_df, on=['code'])
		df = df.rename(columns={'name': 'cname'})
		df[df.select_dtypes(['int64']).columns] = df[df.select_dtypes(['int64']).columns].astype('uint8')
		df[df.select_dtypes(['float64']).columns] = df[df.select_dtypes(['float64']).columns].astype('float32')
		df[df.select_dtypes(['object']).columns] = df[df.select_dtypes(['object']).columns].astype(str)
		df.index = df['code']
		day = 'quota_' + str(day).replace('-', '')
		for col in ['code', 'date']:
			del df[col]
		try:
			df.to_hdf(os.path.join(CACHE_PATH, 'quota.h5'), day, format='table', complevel=4, complib='blosc')
		except:
			pass


def mysql_data():
    print('time local time:{}'.format(time.localtime()))
    # exit(0)
    print(type(time.localtime()))
    ver = time.strftime("%Y-%m-%d", time.localtime())
    print('now:{}'.format(datetime.datetime.now()))
    print('now type:{}'.format(type(datetime.datetime.now())))
    ver = datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d")
    ver = datetime.datetime.strftime(datetime.datetime.today(),"%Y-%m-%d")
    # 三种方式是一样的
    print('ver:{}'.format(ver))
    print(type(ver))
    # exit(0)
    try:
        hdf = pd.HDFStore(os.path.join(CACHE_PATH, 'quota.h5'))
        DAY = hdf.keys()[-1]
        print('DAY:{}'.format(DAY))
        hdf.close()
        day = DAY.split('_')[-1]
        DAY = day[0:4] + '-' + day[4:6] + '-' + day[6:]
    except:
        DAY = '2019-01-01'
    days_df = pd.read_sql("""
            select trade_days from calendar where trade_days > '{}' and trade_days<= '{}'
            """.format(DAY, ver), engine)

    ds = days_df['trade_days'].values
    for day in ds:
        print(day)
        mysql_hdf(day)

mysql_data()
