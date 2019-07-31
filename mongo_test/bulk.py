#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient

# 库名
db = MongoClient('mongodb://127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456')
db.admin.authenticate('root', '123456')
# test集合插入
# db.bulk_test.insert_many([{'i': i} for i in range(10000)]).inserted_ids
# db.test.count()
#有条理的大规模数据写入
bulk = db.bulk_test.initialize_ordered_bulk_op()
# Remove all documents from the previous example.
bulk.find({}).remove()
bulk.insert({'_id': 1})
bulk.insert({'_id': 2})
bulk.insert({'_id': 3})
# 更新
bulk.find({'_id': 1}).update({'$set': {'foo': 'bar'}})
#插入替换
bulk.find({'_id': 4}).upsert().update({'$inc': {'j': 1}})
# 替换
bulk.find({'j': 1}).replace_one({'j': 2})
# execute是执行
result = bulk.execute()
print(result)

# 存在异常 的处理
from pymongo.errors import BulkWriteError

# 缓存队列
bulk = db.test.initialize_ordered_bulk_op()
# 查找j=2 然后替换成j=5
bulk.find({'j': 2}).replace_one({'i': 5})
# 插入id＝4
bulk.insert({'_id': 4})
bulk.find({'i': 5}).remove_one()
try:
    bulk.execute()
except BulkWriteError as bwe:
    print(bwe.details)

from pymongo.errors import BulkWriteError

bulk = db.test.initialize_unordered_bulk_op()
bulk.insert({'_id': 1})
bulk.find({'_id': 2}).remove_one()
bulk.insert({'_id': 3})
bulk.find({'_id': 4}).replace_one({'i': 1})
try:
    bulk.execute()
except BulkWriteError as bwe:
    print(bwe.details)

# 初始化队列
bulk = db.test.initialize_ordered_bulk_op()
bulk.insert({'a': 0})
bulk.insert({'a': 1})
bulk.insert({'a': 2})
bulk.insert({'a': 3})
try:
    bulk.execute({'wtimeout': 1})
except BulkWriteError as bwe:
    print(bwe.details)
