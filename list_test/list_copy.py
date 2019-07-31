#! /user/bin/env python
# -*- coding=utf-8 -*-

import copy


def change_list(list_tmp):
    list_tmp.append('list_tmp')
    return True


def change_list_2(list_tmp):
    list_tmp = list_tmp.copy()
    list_tmp.append('list_tmp_2')
    return True


def test_1():
    """
    列表的复制,直接复制还是绑定，需要copy才能分离开
    :return:
    """
    lists = ['pe', 'ps', 'amount']
    list2 = lists
    list2.append('like')
    print(lists)

    list3 = lists.copy()
    list3.append('likess')
    print(lists)

    # 经过函数也会改变原来的list
    flag = change_list(list_tmp=lists)
    print(lists)

    # 在函数内经过复制就不会改变原来的list
    flag2 = change_list_2(list_tmp=lists)
    print(lists)
test_1()
