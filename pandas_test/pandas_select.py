#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
选中某些值
"""

import pandas as pd


def select():
    """
    根据一个数值选取另一个数值
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    hqs = pd.DataFrame(pd_dict)
    print(hqs)
    rate0 = hqs.loc[hqs['code']=='000001','rate0'].values[0]
    print(rate0)
    print(type(rate0))
select()
