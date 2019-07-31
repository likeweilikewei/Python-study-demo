#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def copy():
    """
    python没有赋值，只有引用，因此不能像传变量一样复制
    df可以用df.copy()进行复制
    :return:
    """
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    df = pd.DataFrame(pd_dict)
    df_tmp = df.copy()
    print('df:{}\n'.format(df))
    print(df.ix[0, 'price'])
    df_tmp.ix[0, 'price'] = 666
    print(df.ix[0, 'price'])
    """可以通过ix进行label的索引"""
    print('df.index:{}\n'.format(df.index))
    print('index type:{}'.format(type(df.index[0])))
copy()
