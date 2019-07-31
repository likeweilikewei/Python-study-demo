#! /user/bin/env python
# -*- coding=utf-8 -*-


"""
args:位置参数
y=1:默然参数
kwargs:命名参数
"""

def foo(x, *args):
    """
    *args：（表示的就是将实参中按照位置传值，多出来的值都给args，且以元祖的方式呈现）
    :param x:
    :param args:
    :return:
    """
    print(x)
    print(args)
foo(1, 2, 3, 4, 5)  # 其中的2,3,4,5都给了args


def foo(x, y=1, *args):
    """
    当args与位置参数和默认参数混用的情况下：（注意三者的顺序）
    默认参数也会占一个位置
    :param x:
    :param y:
    :param args:
    :return:
    """
    print(x)
    print(y)
    print(args)
foo(1, 2, 3, 4, 5)  # 其中的x为1，y=1的值被2重置了，3,4,5都给了args


def foo(x, *args, y=1):
    """
    示例二、（三者顺序是:位置参数、*args、默认参数）
    除了x占了一个参数，其余参数全部被args占用了
    :param x:
    :param args:
    :param y:
    :return:
    """
    print(x)
    print(args)
    print(y)
foo(1, 2, 3, 4, 5)  # 其中的x为1，2,3,4,5都给了args,y按照默认参数依旧为1


def foo(x, y, z):
    """
    *开头的元组会一一对应传值
    :param x:
    :param y:
    :param z:
    :return:
    """
    print(x)
    print(y)
    print(z)
foo(*(1, 2, 3))  # 其中的*（1,2,3）拆开来看就是：foo（1,2,3），都按照位置传值分别传给了x,y,z
