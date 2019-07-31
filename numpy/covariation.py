#! /usr/bin/env python
# -*-coding=utf-8-*-

import random
import numpy as np


def test_1():
    x = [4, 2, 6]
    y = [2, 1, 3]
    X = np.vstack((x, y))
    print('X: {}\n'.format(X))
    cov = np.cov(X)
    print('cov: {}'.format(cov))
test_1()


def test_2():
    x = []
    for i in range(10):
        x.append(random.randint(0,100))
    print(x)
    y = []
    for j in x:
        y.append(j*3)
    print(y)

    # 得到相关向量矩阵
    X = np.vstack((x, y))
    print('X: {}\n'.format(X))

    # 得到协方差矩阵
    cov = np.cov(X)
    print('cov: {}'.format(cov))

    # 期望
    S = np.mean(X, axis=0)
    print(S)
test_2()


def get_one():
    """
    取ndarray的一个
    :return:
    """
    _x = [2, 4, 5]
    _y = np.ndarray(_x)
    print(_y[0])
# get_one()
