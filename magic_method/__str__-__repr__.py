#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
__str__定义对类的实例调用str()时的行为。
而__repr__定义对类的实例调用repr()的行为，这两者的区别就是repr面向机器，str面向人。
定义类的输出的时候经常会使用这两个其中的魔法。
"""


class Apple:
    def __init__(self,name,size):
        self.__name = name
        self.__size = size

    def __str__(self):
        return '{}:{}'.format(self.__name,self.__size)

apple = Apple('a','20')
print(apple)
