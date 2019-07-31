#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd
import numpy as np
from datetime import datetime


def column():
    # 第一种方式利用dict和column：[]加载
    dict1 = {'col1': [1,None], 'col2': [2,4]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df1 = pd.DataFrame(dict1)
    print(df1)
    print('\n')

    # 第二种方式用numpy.array生成
    df2 = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['col1', 'col2'], index=['a', 'b'])
    print(df2)
    print('\n')

    # 第三种方式用二维数组生成
    df3 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'], index=['a', 'b'])
    print(df3)
    print('\n')

    # 创建一列
    df4 = pd.DataFrame([1, 2, 3, 4, 5], columns=['cols'], index=['a', 'b', 'c', 'd', 'e'])
    print(df4)
    print('\n')

    # 创建多行
    df5 = pd.DataFrame([[1, 2, 3, 4, 5]], columns=['col1','col2','col3','col4','col5'], index=['a', 'b', 'c', 'd', 'e'])
    print(df5)
    print('\n')
    df6 = pd.DataFrame([[1, 2, 3, 4, 5]], columns=['col1','col2','col3','col4','col5'], index=['a'])
    print(df6)
    print('\n')

    # 第四种方式，一个dict为一行，用[]连接起来创建多行,某个元素缺少会用NaN来代替生成
    df7 = pd.DataFrame([{'col1':None,'col2':2},{'col1':3,'col2':4}], index=['a', 'b'])
    print(df7)
    print('\n')

    df8 = pd.DataFrame({})
    print(df8)
    df8.append(df7)
    print('df8:{}'.format(df8))
    print(df7.append(df8))
    print(df8.append(df7))

column()
print(datetime.now())
