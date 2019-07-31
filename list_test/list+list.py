#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_1():
    """
    +和extend的不同地方就是extend会改变原来的列表并且不返回值，+会返回一个新列表，不会改变原来的列表
    :return:
    """
    lists = ['pe', 'ps', 'amount']
    old_lists = ["stkRealTimeState:*->shrCd", "stkRealTimeState:*->shrNm"]
    list_new = lists + old_lists
    print(list_new)
    print(lists)
    lists.append('likew')
    list_new_2 = lists
    lists.extend(old_lists)
    print('list + list = {}'.format(list_new))
    print('list.append(str) = {}'.format(list_new_2))
    print('list.extend(list) = {}'.format(lists))
test_1()
