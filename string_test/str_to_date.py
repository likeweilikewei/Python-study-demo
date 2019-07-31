#! /user/bin/env python
# -*- coding=utf-8 -*-

from datetime import date
import datetime
import time


"""
字符串和日期之间的转换
"""
# date to str
print(time.strftime("%Y-%m-%d %X", time.localtime()))
# str to date
t = time.strptime("2009 - 08 - 08", "%Y - %m - %d")
y, m, d = t[0:3]
print(y, type(y))
print(datetime.datetime(y, m, d))

# str to date
t1 = time.strptime('20180124', '%Y%m%d')
y, m, d = t1[:3]
print(datetime.datetime(y, m, d))

# str to date
day = '2018-01-25'
t2 = datetime.datetime.strptime(day, '%Y-%m-%d')
print(t2, type(t2))
print(datetime.date.isoformat(t2))


def date_compare():
    """
    日期比大小直接用string就可以了
    :return:
    """
    t1 = '20180101'
    t2 = '20180202'
    t3 = '20150306'
    t4 = '2005-04-05'
    if t2 > t1 and t1 > t3 and t3 >t4:
        print('yes')
    else:
        print('no')
date_compare()
