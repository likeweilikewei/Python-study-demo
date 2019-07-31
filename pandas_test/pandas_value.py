#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
选中某些值
"""

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
    hq = hqs.loc[hqs.code.isin(['000002','000003'])]
    print(hq)
# copy()


def value():
    """
    python没有赋值，只有引用，因此不能像传变量一样复制
    df可以用df.copy()进行复制
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    hqs = pd.DataFrame(pd_dict)
    print(hqs['rate0'][0])
    print(type(hqs['rate0'][0]))
    # 这样没有办法直接指向-1,如有需要，用values[-1]
    print(hqs)
    # 都相当于获得了一个一行的df
    hq = hqs[hqs['code']=='000001']
    s = hqs.loc[hqs['code']=='000001']
    print(hq)
    print(type(hq))
    print(s)
    print(type(s))
    # 都是获得了一哥series
    print('----------------------')
    print(s['name'])
    print(type(s['name']))
    print(s['name'].values[0])

    print(hq['name'])
    print(type(hq['name']))
    print('------------------------')

    print(hqs.loc[hqs['code']=='000001','name'])
    print(type(hqs.loc[hqs['code']=='000001','name']))
    # 获得其中的某个值
    print(hqs.loc[hqs['code']=='000001','name'].values[0])

    # 获得某列
    print(set(hqs['code']))

    # 获得空df的一列
    blocks = pd.DataFrame(columns=['inst', 'name', 'current_price', 'cost_price', 'quantity',
                                           'quantity_sell', 'profit_count', 'profit', 'market_value',
                                           'cost_value', 'status','hold_days','percent'])
    print(set(blocks['inst']))
    print(set(hqs['code'])-set(blocks['inst']))

# value()


def value2():
    """
    空df用loc的时候返回[]
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    ss = pd.DataFrame(pd_dict)
    print(ss[ss['code'].isin([1])])
    print(type(ss[ss['code'].isin(['000001','000002'])]))
    result = pd.DataFrame(columns=['inst', 'name', 'current_price', 'cost_price', 'quantity',
                                   'quantity_sell', 'profit_count', 'profit', 'market_value',
                                   'cost_value', 'status', 'hold_days', 'percent'])
    print(result.to_dict())
    ss = pd.DataFrame( {'inst': {}, 'name': {}, 'current_price': {}, 'cost_price': {}, 'quantity': {}, 'quantity_sell': {}, 'profit_count': {}, 'profit': {}, 'market_value': {}, 'cost_value': {}, 'status': {}, 'hold_days': {}, 'percent': {}})
    # print(ss)
    print(result)
    s1 = result.loc[result['inst'].isin(['000001'])]
    print('------------------')
    print(s1)

    s = ss.loc[ss['inst'].isin(['000001'])]
    print(s)
# value2()


def value3():
    """
    空df用loc的时候返回[]
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    ss = pd.DataFrame(pd_dict)
    values = ss['code'].values
    print(values)
    print(values[0])
    print(values[-1])
    print(type(values))
    # 可以用values访问最后一个数据
    print(ss['inc'].values[-1])
    # 这样也可以直接访问数据
    print(ss['inc'][0])
    # 但是不能这么访问最后一个
    # print(ss['inc'][-1])
    print(ss.loc[:,'inc'][0])
    # loc也不能访问最后一个数据
    # print(ss.loc[:,'inc'][-1])
# value3()


def value4():
    """
    直接将列转化为set,用不用values都可以
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    ss = pd.DataFrame(pd_dict)
    values = ss['code'].values
    print(values)
    print(type(values))
    """
    ['000001' '000002' '000003']
    <class 'numpy.ndarray'>
    """
    print(set(ss.code))
    print(set(ss.code.values))
    print(set(ss['code']))
    print(set(ss['code'].values))
value4()
