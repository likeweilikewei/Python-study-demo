#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_1():
    """
    切片的时候前面的包含，最后的不含
    :return:
    """
    str1 = 'KDJ金叉的股,票有哪些'
    result = str1[-5:]
    print(result)
test_1()
