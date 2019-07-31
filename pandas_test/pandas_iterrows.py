#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd

pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1], 'rate0': [4, 4.1],
           'rate1': [5, 5.1], 'rate2': [6, 6.1]}
pdData = pd.DataFrame(pd_dict)

"""the iteration generate index and column values, the columns amount must be equal to truth"""


def iterrows():
    for _, row in pdData.iterrows():
        print(row)
        # print(type(row))
        print(row['code'])
        print(row.get('codess'))
        rows = pd.Series(row)  # 转化成Series才可以用索引,没有必要
        print(rows['code'])
        code, inc, name, price, rate0, rate1, rate2 = row
        # print(_, '\nrow:', row, type(row))
        # print('code:', code, 'inc:', inc, 'name:', name, 'price:', price, 'rate:', rate0)

iterrows()


"""最快的迭代方式，在py2里是itertools.izip,在py3里是zip"""
def izip_test():
    inp = [{'c1': 10, 'c2': 100}, {'c1': 11, 'c2': 110}, {'c1': 12, 'c2': 120}]
    df = pd.DataFrame(inp)

    for row_tmp in zip(df.index, df['c1'], df['c2']):
        print(row_tmp)
        print('type_row: {}'.format(type(row_tmp)))
        print(row_tmp[1])

# izip_test()
