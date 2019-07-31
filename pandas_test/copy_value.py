#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def copy():
    """
    python没有赋值，只有引用，因此不能像传变量一样复制
    df可以用df.copy()进行复制
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    hqs = pd.DataFrame(pd_dict)
    print(hqs)
    hqs.loc[hqs['rate1'] == 0, 'rate1'] = hqs.loc[hqs['rate1'] == 0, 'rate2']
    print('/n')
    print(hqs)
copy()
