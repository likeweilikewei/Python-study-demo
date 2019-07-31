#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
判断是否是pandas类型
"""

import pandas as pd


def column():
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '科大讯飞'], 'price': [3, 3.1, 4],
               'rate0': [4, 4.1, 4.6], 'rate1': [5, 5.1, 5.2], 'rate2': [6, 6.1, 6.2]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    print('df:{}'.format(df))
    if isinstance(df,pd.DataFrame):
        print('yes')
    else:
        print('no')
column()
