# coding:utf-8
'''
@author: baocheng
'''
from zdreams.mysql_test.dbConnecttion.MySqlConn import Mysql
from _sqlite3 import Row
import time



# sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
# result = mysql.getAll(sqlAll)
# if result:
#     print("get all")
#     for row in result:
#         print("%s\t%s" % (row["uid"], row["goodsname"]))
# sqlAll = "SELECT tb.uid as uid, group_concat(tb.goodsname) as goodsname FROM ( SELECT goods.uid AS uid, IF ( ISNULL(goodsrelation.goodsname), goods.goodsID, goodsrelation.goodsname ) AS goodsname FROM goods LEFT JOIN goodsrelation ON goods.goodsID = goodsrelation.goodsId ) tb GROUP BY tb.uid"
# result = mysql.getMany(sqlAll, 2)
# if result:
#     print("get many")
#     for row in result:
#         print("%s\t%s" % (row["uid"], row["goodsname"]))
#
# result = mysql.getOne(sqlAll)
# print("get one")
# print("%s\t%s" % (result["uid"], result["goodsname"]))

# 插入多条
# sql1 = 'INSERT INTO users (username, email, password) VALUES(%s,%s,%s)'
# time1 = time.time()
# # 申请资源
# mysql = Mysql()
# values = []
# for i in range(10000,20000):
#     values.append(['{}'.format(i),'{}'.format(i),'{}'.format(i)])
# ids = mysql.insertMany(sql=sql1,values=values)
# print('id:{}'.format(ids))
# # 释放资源
# mysql.dispose()
# print('insert many 100000 cost:{}'.format(time.time()-time.time()))

# time2 = time.time()
# # 申请资源
# mysql = Mysql()
# for j in range(10000,20000):
#     # print(j)
#     mysql.insertOne(sql1,['{}'.format(j),'{}'.format(j),'{}'.format(j)])
# # 释放资源
# mysql.dispose()
# print('insert one 100000 cost:{}'.format(time.time()-time2))

def study_update():
    sql2 = "INSERT INTO users (username, email, password) VALUES(%s,%s,%s) ON DUPLICATE KEY  UPDATE id={},password='{}'".format(1,'like')
    values = ['li','2','2']
    time1 = time.time()
    # 申请资源
    mysql = Mysql()
    ids = mysql.update(sql=sql2,param=values)
    print('id:{}'.format(ids))
    # 释放资源
    mysql.dispose()
    print('insert many 100000 cost:{}'.format(time.time()-time.time()))
study_update()
