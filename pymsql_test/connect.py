#! /usr/bin/env python
# -*-coding=utf-8-*-
import time
import pymysql
from datetime import datetime
from contextlib import contextmanager

MYSQL_PATH = 'mysql+mysqldb://root:123456@127.0.0.1:3306/quant_new?charset=utf8&local_infile=1'

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'quant_new',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

# Connect to the database
# connection = pymysql.connect(**config)
# connection.autocommit(True)

# sql2 = "INSERT INTO industry_paper_test(name,date,flag) VALUES ('李可威','20181128',0)"
# try:
#     with connection.cursor() as cursor:
#         dates = datetime.now().strftime("%Y%m%d")
#         print(dates)
#         sql = 'SELECT * FROM industry_paper WHERE date={} AND flag = {}'.format(dates,0)
#         cursor.execute(sql2)
#         connection.commit()
#         # results = cursor.fetchall()
#         # print(results)
# except Exception as e:
#     print(e)
# finally:
#     connection.close()

__connection = pymysql.connect(**config)


# 定义回滚和关闭操作
@contextmanager
def cursors():
    cursor_tmp = __connection.cursor()
    try:
        yield cursor_tmp
        __connection.commit()
    except Exception as e:
        __connection.rollback()
        print('sql operation error:{}'.format(e))
        raise Exception('sql operation error:{}'.format(e))
    finally:
        cursor_tmp.close()

dates = datetime.now().strftime("%Y%m%d")
print(dates)
sql = 'SELECT * FROM industry_paper WHERE date={} AND flag = {}'.format(dates,0)
sql2 = "INSERT INTO industry_paper_test(name,date,flag) VALUES ('李可威','20181128',0)"
sql3 = "SELECT name,plate_index,zeroRatio FROM industry_paper WHERE date={} AND flag={} AND zeroRatio<=(SELECT zeroRatio FROM industry_paper WHERE date={} AND flag={} ORDER BY zeroRatio DESC LIMIT {},1) ORDER BY zeroRatio DESC LIMIT {}".format('20181128',1,'20181128',1,0,10)
sql4 = "SELECT zeroRatio FROM industry_paper WHERE date={} AND flag={} ORDER BY zeroRatio DESC LIMIT {},1".format('20181128',1,10)
sql5 = "SELECT name,plate_index,zeroRatio FROM industry_paper WHERE date={} AND flag={} ORDER BY zeroRatio DESC LIMIT {},{}".format('20181128',1,0,10)
__sql = "SELECT name,cash_most_stock,cash FROM industry_paper WHERE date={} AND flag={} AND all_number>=3 AND cash<=(SELECT cash FROM industry_paper WHERE date={} AND flag={} ORDER BY cash DESC LIMIT {},1) ORDER BY cash DESC,name LIMIT {}"

with cursors() as cursor:
    time1 = time.time()
    cursor.execute(sql)
    s = cursor.fetchall()
    print(s)
    print(time.time()-time1)

"""
子查询的分页方式：

随着数据量的增加，页数会越来越多，查看后几页的SQL就可能类似：
SELECT * FROM articles WHERE category_id = 123 ORDER BY id LIMIT 10000, 10

一言以蔽之，就是越往后分页，LIMIT语句的偏移量就会越大，速度也会明显变慢。
此时，我们可以通过子查询的方式来提高分页效率，大致如下：

SELECT * FROM articles WHERE  id >=  
(SELECT id FROM articles  WHERE category_id = 123 ORDER BY id LIMIT 10000, 1) LIMIT 10 
JOIN分页方式

SELECT * FROM `content` AS t1   
JOIN (SELECT id FROM `content` ORDER BY id desc LIMIT ".($page-1)*$pagesize.", 1) AS t2   
WHERE t1.id <= t2.id ORDER BY t1.id desc LIMIT $pagesize; 
经过我的测试，join分页和子查询分页的效率基本在一个等级上，消耗的时间也基本一致。 

但是对于相同值存在的情况下可能会出现分页重复情况，不够严谨
"""