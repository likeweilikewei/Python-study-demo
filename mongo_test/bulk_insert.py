#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient
import time

conn = MongoClient('mongodb://127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456')
conn.admin.authenticate('root', '123456')
db = conn['ztest_bulk']
coll = db.test1
# coll.create_index("title")
bulkop = coll.initialize_ordered_bulk_op()

time1=time.time()
hqDB = conn['ztest_update']


def bulk_test_3():
    for z in range(3600):
        item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        for i in range(20):
            item['{}'.format(i)] = i
        item['x'] = z
        retval = bulkop.find({'field1':z}).upsert().update({'$push':item})
        # bulkop.insert(item)
    bulkop.execute()
bulk_test_3()
print('bulk update cost:{}'.format(time.time()-time1))


def update_or_mongo_by_code():
    for z in range(3600):
        item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        for i in range(20):
            item['{}'.format(i)] = i
        item['x'] = z
        getattr(hqDB, '{}'.format(z)).update({"x": item['x']}, {"$set": item}, upsert=True)
        # hqDB.test1.insert(item)
        # getattr(hqDB, '{}'.format(z)).insert(item)
        # hqDB.test1.update({"dt": item['dt']}, {"$set": item}, upsert=True)
time2 = time.time()
update_or_mongo_by_code()
print('update cost:{}'.format(time.time()-time2))


# hqDB2 = conn['update']


# def update_or_mongo_by_code3():
#     for z in range(3500):
#         item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
#         for i in range(100):
#             item['{}'.format(i)] = i
#         item['x'] = z
#         getattr(hqDB2, '{}'.format(z)).update({"dt": z}, {"$set": item}, upsert=True)
        # hqDB.test1.update({"dt": item['dt']}, {"$set": item}, upsert=True)
# time3 = time.time()
# update_or_mongo_by_code()
# print('update cost:{}'.format(time.time()-time3))
