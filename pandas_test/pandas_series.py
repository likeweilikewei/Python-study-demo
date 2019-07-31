#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def equal_test():
    """
    list可以判断是否相等，严格顺序必须相等
    :return:
    """
    pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4, 4.1], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    df = pd.DataFrame(pd_dict)
    # print('df:{}\n'.format(df))
    pd_dict_2 = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4.3, 4.2], 'rate1': [5, 5.1], 'rate2': [6, 6.1]}
    df2 = pd.DataFrame(pd_dict_2)
    # print(df2)
    # print(df2.sort_values(by='rate0'))
    # df2.sort_values(by='rate0',inplace=True)
    # print(df2)

    # print(list(set(df2.rate0.tolist())))
    # print(type(df2.rate0.values))
    # if df.rate0.tolist() == df2.rate0.tolist():
    #     print('yes')
    # else:
    #     print('no')
    # if [1,2] == [1,2] and [1,1]!=[1,2]:
    #     print('yes')
    # else:
    #     print('no')
    LIST = ['000003.SH', '000002.SZ']
    df3 = pd.DataFrame({'code': LIST, 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1],
               'rate0': [4.3, 4.2], 'rate1': [5, 5.1], 'rate2': [6, 6.1]})
    print(df3)
    df3['code_index'] = df3['code']
    df3 = df3.set_index('code_index')
    print(df3)
    df3 = df3.sort_values(by='code')
    print(df3)
equal_test()
