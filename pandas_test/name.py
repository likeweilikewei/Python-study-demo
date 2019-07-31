#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
对于pandas dataframes的name可以手动设置，默认为None,事实上pandas可以设置任何的字段，在遍历每一行的时候，
每一个seires的Name自动为其索引，通过row.name来进行访问，如果没有设置索引，则为自增数字，
在series中可以设置name,并且只能设置内置字段，不同于pandas，也只能通过row.name来进行访问
"""

import pandas as pd



def index():
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'names': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    df = pd.DataFrame(pd_dict)

    df.name = 'dfsss'
    df.sss = 'sfda'
    # print(df.name)
    # print(df.sss)
    # print(type(df.sss))
    # print('df:{}'.format(df))
    return df


def iters(df):
    def __apply(row):
        print(row.name)
    df.apply(__apply,axis=1)


def series():
    s = pd.Series([1,2,4],name='aaa')
    print(s)
    print('name:{}'.format(s.name))

df = index()
iters(df=df)
# series()
