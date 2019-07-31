#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def column():
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4, 4.1, 4.6], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    df['code_index'] = df['code']
    df = df.set_index('code_index')
    print('df:{}'.format(df))
    # df['li'] = 0
    df = df[['code', 'inc', 'rate0']]
    print(df)
    lists = ['000001', '000003', '000004']
    dfs = df.loc[df.index.isin(lists)]
    print(dfs)
# column()


def column_value():
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4, 4.1, 4.6], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    print(df)
    pd_dict2 = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [5, 5.1, 5.6], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df2 = pd.DataFrame(pd_dict2)
    print(df2)
    df['rate0'] = df2['rate0']
    print(df)
    # df.columns 返回Index，可以通过 tolist(), 或者 list（array） 转换为list
    print(df.columns)
    if 'inc' in df.columns:
        print('yes')
    else:
        print('no')
# column_value()


def column_new():
    """
    新产生一列，并且可以用round
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4.111789, 4.122456, 4.6135], 'rate1': [5, 5.1, 5.2], 'rate2': [10, 10, 10]}
    df = pd.DataFrame(pd_dict)
    print(df)
    df['new'] = round(df['rate0'] / df['rate2'],2)
    print(df)
# column_new()


def column_add():
    """
    新添加一列,以下都可以
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4.111789, 4.122456, 4.6135], 'rate1': [5, 5.1, 5.2], 'rate2': [10, 10, 10]}
    df = pd.DataFrame(pd_dict)
    print(df)
    s = pd.Series([1,3,4])
    df['new'] = [1,3,4]
    print(df)
# column_add()


def column_choose():
    """
    选取列，改变了列名的顺序
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4.111789, 4.122456, 4.6135], 'rate1': [5, 5.1, 5.2], 'rate2': [10, 10, 10]}
    df = pd.DataFrame(pd_dict)
    print(df)
    dfs = df[['inc','code','rate1']]
    print(dfs)
# column_choose()


def column_judge():
    """
    判断列中是否有某一个值
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4.111789, 4.122456, 4.6135], 'rate1': [5, 5.1, 5.2], 'rate2': [10, 10, 10]}
    df = pd.DataFrame(pd_dict)
    print(df)
    print(df.code)
    # <class 'pandas.core.series.Series'>
    print(type(df.code))
    if not df.code.empty:
        print('yes')
    print('df code values:{}'.format(df.code.values))
    # <class 'numpy.ndarray'>
    print(type(df.code.values))
    if '000001' in list(df.code):
        print('has')
    else:
        print('no has')
    print('\n\n')

    pd_dict2 = {'code': [], 'inc': [], 'name': [], 'price': [],
               'rate0': [], 'rate1': [], 'rate2': []}
    df2 = pd.DataFrame(pd_dict2)
    # df2.to
    print('df2:{}'.format(df2))
    print(df2.code)
    print(type(df2.code))
    if df2.code.empty:
        print('no')
    if '000001' in list(df2.code):
        print('has')
    else:
        print('no has')
column_judge()

