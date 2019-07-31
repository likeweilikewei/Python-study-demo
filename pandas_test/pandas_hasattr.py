#! /user/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd


def hasattr_test():
    """
    pandas也可以使用自省（反射）
    dir([obj]):
    调用这个方法将返回包含obj大多数属性名的列表（会有一些特殊的属性不包含在内）。obj的默认值是当前的模块对象。
    hasattr(obj, attr):
    这个方法用于检查obj是否有一个名为attr的值的属性，返回一个布尔值。
    getattr(obj, attr):
    调用这个方法将返回obj中名为attr值的属性的值，例如如果attr为'bar'，则返回obj.bar。
    setattr(obj, attr, val):
    调用这个方法将给obj的名为attr的值的属性赋值为val。例如如果attr为'bar'，则相当于obj.bar = val。
    :return:
    """
    pd_dict = {'code': ['000001', '000002', '000003'], 'inc': [1, 1.1, 2], 'name': ['平安银行', '万科A', '工商银行'], 'price': [3, 3.1, 5.4],
               'rate0': [4, 4.1, 5.2], 'rate1': [0, 5.1, 0.0], 'rate2': [6, 6.1, 18]}
    hqs = pd.DataFrame(pd_dict)
    print(hqs)
    if hasattr(hqs,'empty'):
        print('yes')
    else:
        print('no')
    print(getattr(hqs,'empty'))
hasattr_test()
