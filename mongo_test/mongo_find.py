#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('mongodb://root:123456@127.0.0.1:3717')
hqDB = conn['pol']

# 返回一个文档
one_data = hqDB.header.find_one()
# print('one_data:', one_data)
# print('one_data 里的pe是：', one_data['boll'])

# 返回所有文档
all_data = hqDB.header.find({'screneType': 17305}, {'_id': 0})
for i in all_data:
    print(i)
# print('all data:{}'.format(all_data))
