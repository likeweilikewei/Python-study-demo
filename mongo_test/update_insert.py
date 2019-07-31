#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient
import time

conn = MongoClient('mongodb://root:123456@127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456',maxPoolSize=5000,minPoolSize=4000)
# conn.admin.authenticate('root', '123456')
hqDB = conn['update_test2']
perfix = 'test_real_{}'.format('000001')



def update_or_mongo_by_code(y):
    item = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    # getattr(hqDB, perfix).update({"dt": '20181112'}, {"$set": item}, upsert=True)
    # hqDB.update_test.update({"field1": y}, {"$set": item}, upsert=True)
    hqDB.update_test.insert_one(item)

# update_or_mongo_by_code()
# getattr(hqDB, perfix).update({"dt": '20181112'}, {"$set": item}, upsert=True)

time1 = time.time()
for i in range(10000):
    update_or_mongo_by_code(i)
print('update cost:{}'.format(time.time()-time1))

# db = MongoClient('mongodb://127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456')
# db.admin.authenticate('root', '123456')
# db = conn['test_ceshi_hq']
# bulk = db.bulk_test_ceshi_hq.initialize_ordered_bulk_op()
#
# perfix2 = 'bulk_test_real_{}'.format('000001')
#
# time2 = time.time()
#
#
# def bulk_test():
#     for j in range(10):
#         bulk.find({}).update({'$set': item})
#     bulk.exexute()
# bulk_test()
# print('bulk update cost:{}'.format(time.time() - time2))



conn = MongoClient('mongodb://127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456')
conn.admin.authenticate('root', '123456')
db = conn['bulk_test']
coll = db.myCollection
bulkop = coll.initialize_ordered_bulk_op()
time3 = time.time()


def bulk_test_2():
    for x in range(10000):
        retval = bulkop.find({'field1':x}).upsert().update({'$push':item})
        # bulkop.insert(item)
    bulkop.execute()
# bulk_test_2()
# print('bulk cost:{}'.format(time.time()-time3))


from pymongo import WriteConcern
conn = MongoClient('mongodb://127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456')
conn.admin.authenticate('root', '123456')
db = conn['bulk_test2']
db=db.get_collection('bulk_test2',write_concern=WriteConcern(w=0))
bulkop2 = db.initialize_ordered_bulk_op()

time4=time.time()
def bulk_test_3():
    for z in range(10000):
        retval = bulkop2.find({'field1':z}).upsert().update({'$push':item})
        # item['x'] = z
        # bulkop.insert(item)
    bulkop2.execute()
# bulk_test_3()
# print('bulk cost:{}'.format(time.time()-time4))
