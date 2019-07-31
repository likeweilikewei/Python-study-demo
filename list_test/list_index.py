#! /user/bin/env python
# -*- coding=utf-8 -*-


def list_index():
    lists = ['pe', 'ps', 'amount', 'ps']
    old_lists = ["stkRealTimeState:*->shrCd", "stkRealTimeState:*->shrNm", "stkRealTimeState:*->nMatch",
                 "stkRealTimeState:*->riseAndFallRate"]
    print(lists.index('ps'))
    print(lists.index('pe'))

"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
同时列出数据和数据下标，一般用在 for 循环当中
Python 2.3. 以上版本可用，2.6 添加 start 参数。
enumerate(sequence, [start=0])
"""


def list_index_2():
    lists = ['a', 'b', 'c', 'a']
    a_index = [i for i, x in enumerate(lists) if x == 'c']
    print('a_index:{}'.format(a_index))
    if a_index:
        print('[] is true')
    else:
        print('[] is false')

list_index()
