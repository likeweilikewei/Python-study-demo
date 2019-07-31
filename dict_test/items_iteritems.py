#!/usr/bin/env python
# -*-coding=utf-8-*-

"""
items()方法是将字典中的每个项分别做为元组，添加到一个列表中，
形成了一个新的列表容器。如果有需要也可以将返回的结果赋值给新变量，这个新的变量就会是一个列表数据类型。
python字典的iteritems方法作用：与items方法相比作用大致相同，只是它的返回值不是列表，而是一个迭代器
"""


def keys():
    a = {'7':7,'2':2,'3':3,'4':4,'5':5,'6':6}
    for i in a.items():
        print(i)
        print(type(i))
    for i,j in a.items():
        print(i,j)
        print(type(i),type(j))
    # py3放弃iteritems
    # for i,j in a.iteritems():
    #     print(i,j)
keys()
