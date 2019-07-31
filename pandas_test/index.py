#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def index():
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    df = pd.DataFrame(pd_dict)
    print('df:{}'.format(df))
    print(df.ix[0, 'price'])
    df.ix[0, 'price'] = 666
    print(df.ix[0, 'price'])
    """可以通过ix进行label的索引"""
    print('df.index:{}\n'.format(df.index))
    print('index type:{}'.format(type(df.index[0])))
# index()


def reindex():
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    df = pd.DataFrame(pd_dict)
    # print('df:{}'.format(df))
    df = df.set_index('code')
    df['li'] = 0
    print(df)

    pd_dicts = {'code': ['000001', '000003'], 'inc': [0.111, 0.111], 'name': ['平安银行', '万科A'], 'price': [0.111, 0.111],
               'rate00': [0.111, 0.111], 'rate10': [0.111, 0.111], 'rate20': [0.111, 0.111]}
    dfs = pd.DataFrame(pd_dicts)
    dfs = dfs.set_index('code')
    print(dfs)

    # 赋值的时候只能一个一个赋值
    for i in dfs.index:
        if i in df.index:
            df.loc[i, 'rate0'] = dfs.loc[i,  'rate00']
    print(df)

    print(df[df.rate0>1])
# reindex()


def operation():
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    print('df:{}'.format(df))
    df = df.set_index('code')
    # df['li'] = 0
    print(df)
# operation()


def operation1():
    """
    根据索引截取行
    :return:
    """
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict,index=['a','b'])
    print('df:{}'.format(df))
    df_tmp = df.loc['a']
    print(df_tmp)
operation1()
