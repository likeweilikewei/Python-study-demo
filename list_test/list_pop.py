#! /user/bin/env python
# -*- coding=utf-8 -*-


def list_index():
    lists = ['pe', 'ps', 'amount', 'ps']
    old_lists = ["stkRealTimeState:*->shrCd", "stkRealTimeState:*->shrNm", "stkRealTimeState:*->nMatch",
                 "stkRealTimeState:*->riseAndFallRate"]
    print(lists)
    lists.pop()
    print(lists)

list_index()
"""pop是弹出最后一个元素，也可以指定index弹出"""


def while_list():
    lists = ['a', 'b', 'c']
    while lists:
        x = lists.pop()
        print(x)

while_list()
