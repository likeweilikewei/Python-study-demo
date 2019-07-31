#! /user/bin/env python
# -*- coding=utf-8 -*-

import timeit
import dis

"""可以用< 也可以用issubset来判断一个set是否是另一个的子集"""


def set_issubset():
    a = set('abcd')
    b = set('abcdefg')
    print('a:{}'.format(a))
    print('b:{}'.format(b))
    dicts = {'test': set()}
    dicts['test'].add('a')
    dicts['test'].add('b')
    print("dicts['test']: {}".format(dicts['test']))
    results = dicts['test'] < a
    print('< test result:{}'.format(results))
    result = dicts['test'].issubset(a)
    print('result:{}'.format(result))
    c = set(['a', 'b'])
    result3 = c < a
    print('result3:{}'.format(result3))

# set_issubset()


def f():
    return set([1, 2, 3])


def h():
    return set((1, 2, 3))


def g():  # set literrals
    return {1, 2, 3}


"""
Python 代码是先被编译为字节码后，再由Python虚拟机来执行字节码， Python的字节码是一种类似汇编指令的中间语言，
 一个Python语句会对应若干字节码指令，虚拟机一条一条执行字节码指令， 从而完成程序执行。
Python dis 模块支持对Python代码进行反汇编， 生成字节码指令。
最快的是直接创建
"""


def create_set():
    f_time = min(timeit.repeat(f))
    g_time = min(timeit.repeat(g))
    h_time = min(timeit.repeat(h))
    dis.dis(f)
    dis.dis(h)
    dis.dis(g)
    print('f time:{}'.format(f_time))
    print('h time:{}'.format(h_time))
    print('g time:{}'.format(g_time))

# create_set()


def set_operation():
    a =set([1, 3, 2, 4])
    b = set([3,4,5,6])
    print('a-b:{}'.format(a-b))
    if a-b:
        print('not empty')
    else:
        print('empty')
    print(list(a))
    for i in a-b:
        print(i)
set_operation()
