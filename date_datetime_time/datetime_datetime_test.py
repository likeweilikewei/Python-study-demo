#! /usr/bin/env python
# -*-coding=utf-8-*-

from datetime import datetime



def weelday():
    """
    获取一周的第几天，周一是第0天
    :return:
    """
    times = datetime.now()
    print(times)
    print(times.weekday())
# weelday()


def day_test():
    """
    获取一个月的第几天，13号是第13天
    :return:
    """
    times = datetime.now()
    print(times)
    print(times.day)
# day_test()


def datetime_to_string():
    """
    mysql的date可以用str来查找
    :return:
    """
    a = '2018-02-14 16:19:18'
    # 向上转成datetime的时候格式不能少也不能多
    s1 = datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
    print('s1:{}'.format(s1))
    print('s1 type:{}'.format(type(s1)))
    a1 = '2018-02-15'
    s2 = datetime.strptime(a1,'%Y-%m-%d')

    print('s2:{}'.format(s2))
    print('s2 type:{}'.format(type(s2)))

    s3 = s2.date()
    print('s3:{}'.format(s3))
    print('s3 type:{}'.format(type(s3)))

    # 将datetime转化为str
    if isinstance(s1,datetime):
        b1 = datetime.strftime(s1,'%Y-%m-%d %H:%M:%S')
        print('b1:{}'.format(b1))
        print('b1 type:{}'.format(type(b1)))
        print('s1{}'.format(s1))
        # 但是向下转成str的时候可以少
        b2 = datetime.strftime(s1,'%Y-%m-%d')
        print('b2:{}'.format(b2))
        print('b2 type:{}'.format(type(b2)))
datetime_to_string()
