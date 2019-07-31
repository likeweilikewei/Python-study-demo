#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd

pd_dict = {'code': ['000001', '000002'], 'inc': [1, 1.1], 'name': ['平安银行', '万科A'], 'price': [3, 3.1], 'rate0': [4, 4.1],
           'rate1': [5, 5.1], 'rate2': [6, 6.1]}
pdData = pd.DataFrame(pd_dict)
print(pdData)

print(pdData.values.tolist())
