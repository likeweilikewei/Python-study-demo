#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
从目前来看，__和_怎么传都行
"""


def test_1(__file):
    print(__file)
    return __file


def test_4(__file):
    print(__file)
    _file = __file
    return _file


def test_2(_file):
    print(_file)
    return _file


def test_3(file):
    print(file)
    return file


def tests():
    file = 'li kewei'
    result_1 = test_1(__file=file)
    result_2 = test_2(_file=file)
    result_3 = test_3(file=file)
    result_4 = test_4(__file=file)
    print('result_1: {}'.format(result_1))
    print('result_2: {}'.format(result_2))
    print('result_3: {}'.format(result_3))
    print('result_4: {}'.format(result_4))
    __file = 'likes milk.'
    result_5 = test_1(__file=__file)
    result_6 = test_2(_file=__file)
    result_7 = test_3(file=__file)
    result_8 = test_4(__file=__file)
    print('\nresult_5: {}'.format(result_5))
    print('result_6: {}'.format(result_6))
    print('result_7: {}'.format(result_7))
    print('result_8: {}'.format(result_8))
tests()
