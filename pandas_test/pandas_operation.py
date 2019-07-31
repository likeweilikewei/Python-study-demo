#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def merge():
    """
    合并指定列相同的两行
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000001'], 'inc': [1, 1.1, 1.2],
               'name': ['平安银行', '万科A', '平安银行'], 'price': [3, 3.1, 2.1],
               'rate0': [4, 4.1, 3.2], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2],
               'event': [1, 2, 1]}
    df = pd.DataFrame(pd_dict)
    ss = df.groupby(['code', 'event'])
    print(*ss)
# merge()


def operation():
    """
    对指定行和列做运算
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 1.2],
               'name': ['平安银行', '万科A', '平安银行'], 'price': [3, 3.1, 2.1],
               'rate0': [4, 4.1, 3.2], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2],
               'event': [1, 2, 1], 'close': [0, 0, 0]}
    df = pd.DataFrame(pd_dict)
    df = df.set_index('code')
    print(df)
    # print(df.loc[df.event==1, 'close'])
    # exit(0)
    df.loc[df.event==1, 'close'] = df.loc[df.event==1, 'rate0'] + df.loc[df.event==1, 'rate1']
    df.loc[df.event==2, 'close'] = df.loc[df.event==2, 'rate0'] + df.loc[df.event==2, 'rate2']
    print(df)
    print(len(df))
operation()
