#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd

pd_dict = {'code': ['000001', None, '123456', '234567'], 'inc': [1, 1.1, 12, 1.6],
           'name': ['平安银行', '万科A', 'like', 'likewe'], 'price': [3, 3.1, 5.5, 1.3],
           'rate0': [4, 4.1, None, 802], 'rate1': [5, 5.1, 1.1, 10], 'rate2': [6, 6.1, 1.3, 9.6]}

dfs = pd.DataFrame(pd_dict)
print('df:{}\n'.format(dfs))


def df_del(df=dfs):
    """
    删除某一行为某个值的元素
    :param df:
    :return:
    """
    print((True ^ df['rate0'].isin([None])))
    print(type((True ^ df['rate0'].isin([None]))))
    df = df[(True ^ df['rate0'].isin([None]))]
    print(df)
# df_del()


def del_index():
    """
    测试删除一行之后index是否有变化
    :return:
    """
    for i in dfs.index:
        print('index:{}'.format(i))
    dfs.drop(0, axis=0, inplace=True)
    print('\nnew dfs:\n{}'.format(dfs))
# del_index()


def dropna():
    """
    how=all的时候删除一行全为空的行，any为有空就删除
    :return:
    """
    dfs.dropna(inplace=True)
    print(dfs)
dropna()
