#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_1():
    str1 = 'KDJ金叉的股,票有哪些'
    if '股,票' in str1:
        print('yes')
    else:
        print('no')
    if '_' in 'jaj_12':
        print('yes')
    else:
        print('no')
test_1()
