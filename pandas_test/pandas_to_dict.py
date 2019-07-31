#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd

pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1], 'rate0': [4, 4.1],
           'rate1': [5, 5.1], 'rate2': [6, 6.1]}
pdData = pd.DataFrame(pd_dict)
print(pdData)
print(pdData.to_dict())
# T会让索引为键，默认列名为键
dict_country = pdData.set_index('code').T.to_dict()
print(dict_country)
# 不指定索引会使用默认的索引为键
print(pdData.T.to_dict())
print(pdData.T)

# 将空df转为dict
blocks = pd.DataFrame(columns=['inst', 'name', 'current_price', 'cost_price', 'quantity',
                                               'quantity_sell', 'profit_count', 'profit', 'market_value',
                                               'cost_value', 'status', 'hold_days', 'percent'])
print(blocks.to_dict())
dict_country = blocks.set_index('inst').T.to_dict()
print(dict_country)
