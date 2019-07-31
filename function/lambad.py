#!/usr/bin/env python
# -*-coding=utf-8-*-
from functools import reduce
"""
需要两个参数,第一个是一个处理函数,第二个是一个序列(list,tuple,dict)
map()

将序列中的元素通过处理函数处理后返回一个新的列表
filter()

将序列中的元素通过函数过滤后返回一个新的列表
reduce()

将序列中的元素通过一个二元函数处理返回一个结果
将上面三个函数和lambda结合使用
"""


def lambda_test():
    result = lambda x: x * x
    x = result(2)  # return 4
    print(x)

    li = [1, 2, 3, 4, 5]
    print(li)
    # 序列中的每个元素加1
    x1 = map(lambda x: x + 1, li)  # [2,3,4,5,6]
    print('map:{}'.format(list(x1)))

    # 返回序列中的偶数,返回的对象是可以迭代的
    x2 = filter(lambda x: x % 2 == 0, li)  # [2, 4]
    for i in x2:
        print(i)
    print('filter:{}'.format(list(x2)))

    # 返回所有元素相乘的结果
    x3 = reduce(lambda x, y: x * y, li)  # 1*2*3*4*5 = 120
    print('reduce:{}'.format(x3))
lambda_test()
