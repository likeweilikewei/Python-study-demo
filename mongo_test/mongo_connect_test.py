#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient

conn = MongoClient('mongodb://root:123456@127.0.0.1:3717')
hqDB = conn['hq']

one_data = hqDB.hq_D_bfq_000001.SZ.find_one()
print('one_data:', one_data)
print('one_data 里的pe是：', one_data['boll'])
