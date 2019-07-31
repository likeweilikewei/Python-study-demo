#! /usr/bin/env python
# -*-coding=utf-8-*-


import numpy as np


def numpy_test():
    codes = ['000001','000002','000003']
    c = np.array(codes)
    print(c==['000001'])
    e = np.array([1,2,3])
    a = [[1,3,2],[2,4,3],[5,3,4]]
    b = np.array(a)
    print(b)
    # b[b >2] = 0
    d = b[c == '000002']
    print(d)
numpy_test()
