#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
行选择
Pandas进行行选择一般有三种方法：

连续多行的选择用类似于python的列表切片
按照指定的索引选择一行或多行，使用loc[]方法
按照指定的位置选择一行多多行，使用iloc[]方法

列选择
列选择比较简单，只要直接把列名传递过去即可，如果有多列的数据，要单独指出列名或列的索引号

第一种，选择单列，选择了电影名称那一列
第二种，通过指定列名选择多列
第三种，非常容易让人混淆的，通过列的索引号选择多列

1. loc——通过行标签索引行数据
1.1 loc[1]表示索引的是第1行（index 是整数）

import pandas as pd
data = [[1,2,3],[4,5,6]]
index = [0,1]
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc[1]
'''
a    4
b    5
c    6
'''

1.2 loc[‘d’]表示索引的是第’d’行（index 是字符）


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc['d']
'''
a    1
b    2
c    3
'''

1.3 如果想索引列数据，像这样做会报错


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc['a']
'''
KeyError: 'the label [a] is not in the [index]'
'''

1.4 loc可以获取多行数据


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc['d':]
'''
   a  b  c
d  1  2  3
e  4  5  6
'''

1.5 loc扩展——索引某行某列


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc['d',['b','c']]
'''
b    2
c    3
'''

1,6 loc扩展——索引某列


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc[:,['c']]
'''
   c
d  3
e  6
'''

当然获取某列数据最直接的方式是df.[列标签]，但是当列标签未知时可以通过这种方式获取列数据。

需要注意的是，dataframe的索引[1:3]是包含1,2,3的，与平时的不同。

2. iloc——通过行号获取行数据
2.1 想要获取哪一行就输入该行数字


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.loc[1]
'''
a    4
b    5
c    6
'''

2.2 通过行标签索引会报错


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.iloc['a']
'''
TypeError: cannot do label indexing on <class 'pandas.core.index.Index'> with these indexers [a] of <type 'str'>
'''

2.3 同样通过行号可以索引多行


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.iloc[0:]
'''
   a  b  c
d  1  2  3
e  4  5  6
'''

2.4 iloc索引列数据


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.iloc[:,[1]]
'''
   b
d  2
e  5
'''

3. ix——结合前两种的混合索引
3.1 通过行号索引


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.ix[1]
'''
a    4
b    5
c    6
'''

3.2 通过行标签索引


import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['d','e']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
print df.ix['e']
'''
a    4
b    5
c    6

"""

import pandas as pd
from copy import deepcopy


def operation1():
    """
    截取行列
    :return:
    """
    pd_dict = {'code': ['000001', '000002','000003'], 'inc': [1, 1.1,2.2], 'name': ['平安银行', '万科A','工商银行'], 'price': [3, 3.1,6.9],
               'rate0': [4, 4.1, 5.3], 'rate1': [5, 5.1, 4.2], 'rate2': [6, 6.1, 7.8]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict,index=['a','b','c'])
    print('df:\n{}\n'.format(df))

    # 行选择
    # 第一种,使用类似于python的列表切片,包括前者不包括后者
    df_tmp = df[:2]
    print('第一种：\n{}\n'.format(df_tmp))

    # 第二种，按照指定的索引选择一行或多行，使用loc[]方法
    # 默认的数字索引可以用[:2]选择前两行，否则需要用索引名进行选择
    df_tmp1 = df.loc['a']
    print('第二种1：\n{}\n'.format(df_tmp1))

    df_tmp2 = df.loc[['a','b']]
    print('第二种2：\n{}\n'.format(df_tmp2))

    #第三种，按照指定的位置选择一行多多行，使用iloc[]方法
    # 这时候就不能用具体的索引名了，必须要用索引号
    df_tmp3 = df.iloc[2,1:3]
    print('第三种1：\n{}\n'.format(df_tmp3))

    df_tmp31 = df.iloc[2,[1,2]]
    print('第三种2：\n{}\n'.format(df_tmp31))

    # 在iloc中:和[]都可以使用，同样：的后者不包括
    df_tmp31 = df.iloc[:2,[1,2]]
    print('第三种2：\n{}\n'.format(df_tmp31))

    # 如果索引号删除，则索引不会自动补齐，这是不能用iloc索引这个索引号了，不认会出错
    df_tmp = deepcopy(df)
    # df_tmp = df_tmp.drop([1],axis=0)
    print('第三种3：\n{}\n'.format(df_tmp))
    # print(df_tmp.columns)
    # print(df_tmp.index)
    """
    enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
    Python 2.3. 以上版本可用，2.6 添加 start 参数,决定下标的开始。
    >>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))       # 下标从 1 开始
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
    """
    # iat和iloc作用一样，at和loc作用一样，下面得到列号和列
    # print(enumerate(df_tmp.columns))
    # for i,j in enumerate(df_tmp.columns):
    #     # print(i,j)
    #     print(df_tmp.iat[0,i])

    # drop函数默认删除行，列需要加axis = 1
    df_tmp = df_tmp.drop(['b'],axis=0)
    print('第三种3：\n{}\n'.format(df_tmp))

    # iloc是选择第二行，索引号乱序或者缺失也不会影响
    """
    iloc[2]的意思是选择第三行的数据，也就是索引号为4的那一行数据，因为iloc[]的计算也是从0开始的，所以iloc[]适用于数据进行了筛选后造成索引号与原来不一致的情况
    loc[]与iloc[]方法之间还有一个巨大的差别，那就是loc[]里的参数是对应的索引值即可，所以参数可以是整数，也可以是字符串。而iloc[]里的参数表示的是第几行的数据，所以只能是整数
    """
    df_tmp4 = df_tmp.iloc[1]
    print('第三种4：\n{}\n'.format(df_tmp4))

    # 列索引
    # 第一种，只要直接把列名传递过去即可，如果有多列的数据，要单独指出列名
    df_tmp11 = df['name']
    print('第一种1：\n{}\n'.format(df_tmp11))

    df_tmp12 = df[['name','code']]
    print('第一种2：\n{}\n'.format(df_tmp12))

# operation1()


def operation2():
    """
    行的实验,loc还可以接受如下的输入，输出相应的行
    :return:
    """
    pd_dict = {'code': ['000001', '000002','000003'], 'inc': [1, 1.1,2.2], 'name': ['平安银行', '万科A','工商银行'], 'price': [3, 3.1,6.9],
               'rate0': [4, 4.1, 5.3], 'rate1': [5, 5.1, 4.2], 'rate2': [6, 6.1, 7.8]}
    # 这样会多出一列不必要的code
    # df = pd.DataFrame(pd_dict, index=pd_dict['code'])
    df = pd.DataFrame(pd_dict,index=['a','b','c'])
    print('df:\n{}\n'.format(df))

    print(df['price']>3)
    print(df.loc[[True,True]])
operation2()
