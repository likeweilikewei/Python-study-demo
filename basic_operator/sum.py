#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
描述
sum() 方法对系列进行求和计算。
语法
以下是 sum() 方法的语法:
sum(iterable[, start])
参数
iterable -- 可迭代对象，如：列表、元组、集合。
start -- 指定相加的参数，如果没有设置这个值，默认为0。
"""


def test_1():
    list_1 = [['李', '可', '威'], ['li', 'ke', 'wei']]
    result1 = sum(list_1, [])
    print('results: {}'.format(result1))
test_1()
