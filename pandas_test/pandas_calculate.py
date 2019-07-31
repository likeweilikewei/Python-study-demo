#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd
import numpy as np
from datetime import datetime


def pct_change():
    """
    计算和前一个数值的涨跌幅
    :return:
    """
    # 第一种方式利用dict和column：[]加载
    dict1 = {'col1': [1,2,3,4,5], 'col2': [None,4,4,None,None]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df1 = pd.DataFrame(dict1)
    df1['col3'] = df1['col1'].pct_change()
    df1['col4'] = df1['col2'].pct_change()
    print(df1)
    df1 = df1.fillna(method='ffill')
    df1 = df1.fillna(0)
    print(df1)
    print('\n')

# pct_change()
# print(datetime.now())


def std_study():
    """
    numpy.std() 求标准差的时候默认是除以 n 的，即是有偏的，np.std无偏样本标准差方式为加入参数 ddof = 1；
    pandas.std() 默认是除以n-1 的，即是无偏的，如果想和numpy.std() 一样有偏，需要加上参数ddof=0 ，
    即pandas.std(ddof=0) ；DataFrame的describe()中就包含有std()，无偏且不能设置；
    :return:
    """
    df = pd.DataFrame([[1, 2, 3, 4, 5, 6], [2, 4, 1, 2, 3, 5], [3, 43, 2, 2, 7, 9]], index=['one', 'two', 'three'],
                      columns=['A', 'B', 'C', 'D', 'E', 'F'])
    print(df)
    # print(df.count(axis=1))
    # print(df.sum(1))
    # print(df.mean())
    # print(df.mode(axis=0))
    # print(df.mode(axis=1))
    print(df.std())
    print(df.std(ddof=0))
    print('\n')
    print(df.describe())
    print('\n')
    # print(np.sqrt())
    l1 = np.array([1, 2, 3])
    print(l1.std())
std_study()


def var_study():
    """
    numpy 中计算的方差就是样本方差本身
    pandas 中计算的方差为无偏样本方差
    :return:
    """
    a = np.array([1, 2, 3, 4, 5])  # 构造np.array对象
    b = pd.Series([1, 2, 3, 4, 5])  # 构造pd.Series对象
    print(a.var(), b.var())  # 求方差
# var_study()


def cov_study():
    """
    协方差
    协方差（Covariance）在概率论和统计学中用于衡量两个变量的总体误差。而方差是协方差的一种特殊情况，即当两个变量是相同的情况。
    :return:
    """
    df = pd.DataFrame([[1, 2, 3, 4, 5, 6], [2, 4, 1, 2, 3, 5], [3, 43, 2, 2, 7, 9]], index=['one', 'two', 'three'],
                      columns=['A', 'B', 'C', 'D', 'E', 'F'])
    print(df)
    print(df.cov())
# cov_study()
