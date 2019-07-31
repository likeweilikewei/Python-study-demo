#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient
import time

conn = MongoClient('mongodb://dds-bp1918c1e66810541.mongodb.rds.aliyuncs.com:3717,dds-bp1918c1e66810542.mongodb.rds.aliyuncs.com:3717/admin?')
conn.admin.authenticate('root', 'joDsbtHeQMGifr4z')
db = conn['ztest']
coll = db.bulk1
# coll.create_index("title")
bulkop = coll.initialize_ordered_bulk_op()

time1=time.time()
hqDB = conn['zupdate_test']
print('start')


def bulk_test_3():
    for z in range(3600):
        item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

        for i in range(20):
            item['{}'.format(i)] = i
        item['x'] = z

        item2 = {
            "dt": "2018-08-07 09:30:00",
            "high": 100.0,
            "low": 100.0,
            "amount": 0.0,
            "vol": "0",
            "close": 100.0,
            "last_close": 100.0,
            "category": "14901",
            "inc": 0.0,
            "open": 100.0,
            "name": 'ss',
            "code": "690007"
        }
        retval = bulkop.find({'field1':z}).upsert().update({'$push':item2})
        # bulkop.insert(item)
    bulkop.execute()
bulk_test_3()
print('bulk update cost:{}'.format(time.time()-time1))




def update_or_mongo_by_code():
    for z in range(3600):
        # item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        item = {
            "dt": "2018-08-07 09:30:00",
            "high": 100.0,
            "low": 100.0,
            "amount": 0.0,
            "vol": "0",
            "close": 100.0,
            "last_close": 100.0,
            "category": "14901",
            "inc": 0.0,
            "open": 100.0,
            "name": 'ss',
            "code": "690007"
        }
        # for i in range(20):
        #     item['{}'.format(i)] = i
        # item['x'] = z
        # getattr(hqDB, '{}'.format(z)).create_index("dt")
        getattr(hqDB, '{}'.format(z)).update({"dt": item['dt']}, {"$set": item}, upsert=True)
        # hqDB.test1.insert(item)
        # getattr(hqDB, '{}'.format(z)).insert(item)
        # hqDB.test1.update({"dt": item['dt']}, {"$set": item}, upsert=True)
time2 = time.time()
update_or_mongo_by_code()
print('update cost:{}'.format(time.time()-time2))
