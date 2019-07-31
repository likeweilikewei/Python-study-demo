#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def column():
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4, 4.1, 4.6], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2],'date':['2019-01-01','2019-01-02','2019-01-03']}
    pd_dict2 = {'code': ['000001', '000002', '000003','000004'], 'inc2': [1, 1.1, 2,3], 'name': ['平安银行', '万科A', '科大讯飞','初音龙牧'], 'price': [3, 3.1, 4,6],
               'rate00': [4, 4.1, 4.6,1.2], 'rate10': [5, 5.1, 5.2,6], 'rate20': [6, 6.1, 6.2,67],'date':['2019-01-01','2019-01-02','2019-01-03','2019-01-04']}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    df2 = pd.DataFrame(pd_dict2)
    # 取并集，没有的字段为NaN
    df_new = df.merge(df2, on=['code', 'date'],how='outer')
    print(df_new)
    print('\n')
    print(df_new.loc[:,'inc'])
    print(type(df_new.loc[:,'inc']))
    # exit(0)
    print(df_new.loc[:,'inc'].values[0])
    print(type(df_new.loc[:,'inc'].values[0]))
    print(df_new.loc[:,'inc'].values[3])
    print(type(df_new.loc[:,'inc'].values[3]))
    print(df_new.iloc[3,3])
    print(type(df_new.iloc[3,3]))
    # 去交集
    df_new_2 = df.merge(df2, on=['code', 'date'],how='inner')
    print(df_new_2)
# column()


def column2():
    """
    默认没有重合字段就是直接拼接，没有的补NaN
    默认列拼接
    :return:
    """
    pd_dict = {'code1': ['000001', '000002', '000003'], 'inc1': [1, 1.1, 2], 'name1': ['平安银行', '万科A', '科大讯飞'], 'price1': [3, 3.1, 4],
               'rate10': [4, 4.1, 4.6], 'rate11': [5, 5.1, 5.2], 'rate12': [6, 6.1, 6.2],'date1':['2019-01-01','2019-01-02','2019-01-03']}
    pd_dict2 = {'code': ['000001', '000002', '000003','000004'], 'inc2': [1, 1.1, 2,3], 'name': ['平安银行', '万科A', '科大讯飞','初音龙牧'], 'price': [3, 3.1, 4,6],
               'rate00': [4, 4.1, 4.6,1.2], 'rate10': [5, 5.1, 5.2,6], 'rate20': [6, 6.1, 6.2,67],'date':['2019-01-01','2019-01-02','2019-01-03','2019-01-04']}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    df2 = pd.DataFrame(pd_dict2)
    # 取并集，没有的字段为NaN
    df_new = df.merge(df2,how='outer')
    print(df_new)
    print('\n\n')
    df_new_2 = df.merge(df2,how='inner')
    print(df_new_2)
column2()
