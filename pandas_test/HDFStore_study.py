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
import string

from quant_backend.models import engine


print(os.path.dirname(__file__))
print(os.path.pardir)
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
print(PROJECT_PATH)
CURRENT_PATH = os.path.join(os.path.dirname(__file__))
# 缓存
CACHE_PATH = os.path.join(CURRENT_PATH, 'cache')
print(CACHE_PATH)


df = pd.DataFrame({
     'int32':    np.random.randint(0, 10**6, 1000),
     'int64':    np.random.randint(10**7, 10**9, 1000).astype(np.int64)*10,
     'float':    np.random.rand(1000),
     'string':   np.random.choice([c*10 for c in string.ascii_uppercase], 1000),
     })
print(df)
# "date": ['20190601', '20190602', '20190603', '20190604', '20190605', '20190606', '20190607', '20190608', '20190609',
#          '20190610']

df2 = pd.DataFrame({
     'int32':    np.random.randint(0, 10**6, 2),
     'int64':    np.random.randint(10**7, 10**9, 2).astype(np.int64)*10,
     'float':    np.random.rand(2),
     'string':   np.random.choice([c*10 for c in string.ascii_uppercase], 2),
     "date":['20190611','20190612']
     })

# print(np.random.rand(10))
# print(type(np.random.rand(10)))

# 大写字母字符串
# print(string.ascii_uppercase)
# for i in string.ascii_upp ercase:
#     print(i)

# df = pd.concat([df] * 10**5, ignore_index=True)

# print(df)
# 创建打开hdf文件有两种方式，一种是HDFStore,一种是pd.read_hdf
# create (or open) an hdf5 file and opens in append mode
# 这种方式查询可以直接用store.select
store = pd.HDFStore(os.path.join(CACHE_PATH, 'storage1.h5'))
# store3 = pd.HDFStore(os.path.join(CACHE_PATH, 'storage3.h5'))

#read_hdf,这种方式的查询都在语句里,直接读取成df
# df_store=pd.read_hdf((os.path.join(CACHE_PATH,'storage1.h5')),'000001')
# print('df store:{}'.format(df_store))

# 有三种方式可以加入数据put append to_hdf
"""
List of columns to create as indexed data columns for on-disk queries, or True to 
use all columns. By default only the axes of the object are indexed. See Query via 
Data Columns. Applicable only to format=’table’.
"""

#默认追加
# store.append('000001', df,format="table",data_columns=['date'])

# put每次都会覆盖之前的内容，也可以设置append=true
# store.put('000001',df)

# hdf默认也是覆盖
df.to_hdf(os.path.join(CACHE_PATH,'storage2.h5'),'000000',format='table')
# 压缩功能有限
df.to_hdf(os.path.join(CACHE_PATH,'storage3.h5'),'000000',format='table', complevel=4, complib='blosc')

# print(store['000001'].shape)

# result = store.get_storer('store_key').table
# print('result:{}'.format(result))
#
# result2 = store.get(key='store_key')
# print('result2:{}'.format(result))
#
# print(type(result2))

# print(df[:2])


# store.append('store_key2', df[:10], data_columns=['int32','int64','string'])
#
# result = store.get_storer('store_key2').table
# print('result:{}'.format(result))
#
# result2 = store.get(key='store_key2')
# print('result2:{}'.format(result))
#
# print(type(result2))
# print(pd.DataFrame(result2))

# print(store.keys())


print(store.info())
# 得到文件内所有的键，是升序排列的
print(store.keys())
store.close()
# store.close()# closes the file
