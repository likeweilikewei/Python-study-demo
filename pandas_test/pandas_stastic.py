#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd

pd_dict = {'code': ['000001', '000002', '123456', '234567'], 'inc': [1, 1.1, 12, 1.6],
           'name': ['平安银行', '万科A', 'like', 'likewe'], 'price': [3, 3.1, 5.5, 1.3],
           'rate0': [4, 4.1, 3.2, 802], 'rate1': [5, 5.1, 1.1, 10], 'rate2': [6, 6.1, 1.3, 9.6]}

df = pd.DataFrame(pd_dict)
print('df:{}'.format(df))


def median():
    # axis = 1,对行进行操作，axis = 0对列进行操作，默认都是对列进行操作
    # 取中位数
    medians = df.median(axis=0)
    print('median: {}'.format(medians))
    print('type:{}'.format(type(medians)))
    print(medians['rate0'])
median()
