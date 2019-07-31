#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def column2():
    """
    默相同字段的表首尾相接
    默认axis=0列索引，索引号出重复
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc1': [1, 1.1, 2], 'name1': ['平安银行', '万科A', '科大讯飞'], 'price1': [3, 3.1, 4],
               'rate10': [4, 4.1, 4.6], 'rate11': [5, 5.1, 5.2], 'rate12': [6, 6.1, 6.2],'date1':['2019-01-01','2019-01-02','2019-01-03']}
    pd_dict2 = {'code': ['000001', '000002', '000003','000004'], 'inc2': [1, 1.1, 2,3], 'name': ['平安银行', '万科A', '科大讯飞','初音龙牧'], 'price': [3, 3.1, 4,6],
               'rate00': [4, 4.1, 4.6,1.2], 'rate10': [5, 5.1, 5.2,6], 'rate20': [6, 6.1, 6.2,67],'date':['2019-01-01','2019-01-02','2019-01-03','2019-01-04']}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict)
    df2 = pd.DataFrame(pd_dict2)
    result1 = pd.concat([df,df2])
    print(df)
    print(df2)
    print('\n')
    print(result1)
    print('\n\n')
    result2 = pd.concat([df,df2],axis=1)
    print(df)
    print(df2)
    print('\n')
    print(result2)
    print(result2.columns)
column2()
