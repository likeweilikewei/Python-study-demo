#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def to_datetime():
    # 第一种方式利用dict和column：[]加载
    dict1 = {'date': ['2019-2-20','2019-2-17'], 'col2': ['2019-2-21','2019-2-16']}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df1 = pd.DataFrame(dict1)
    print(df1)
    df1['date1_new'] = pd.to_datetime(df1['date'])
    df1['date2_new'] = pd.to_datetime(df1['col2'])
    days = (df1['date1_new']-df1['date2_new']).dt.days
    print(days)
to_datetime()
