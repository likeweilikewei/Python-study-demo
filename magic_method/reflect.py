#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
你可以通过定义魔法方法来控制用于反射的内建函数 isinstance 和 issubclass 的行为。下面是对应的魔法方法：

__instancecheck__(self, instance)

检查一个实例是否是你定义的类的一个实例（例如 isinstance(instance, class) ）。

__subclasscheck__(self, subclass)

检查一个类是否是你定义的类的子类（例如 issubclass(subclass, class) ）。

这几个魔法方法的适用范围看起来有些窄，事实也正是如此。我不会在反射魔法方法上花费太多时间，
因为相比其他魔法方法它们显得不是很重要。但是它们展示了在Python中进行面向对象编程（或者总体上使用Python进行编程）时很重要的一点：
不管做什么事情，都会有一个简单方法，不管它常用不常用。这些魔法方法可能看起来没那么有用，但是当你真正需要用到它们的时候，
你会感到很幸运，因为它们还在那儿（也因为你阅读了这本指南！）
"""


class FunctionalList:
    '''一个列表的封装类，实现了一些额外的函数式
    方法，例如head, tail, init, last, drop和take。'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # 如果键的类型或值不合法，列表会返回异常
        if key not in self.values and key not in range(len(self.values)):
            return self.__missing__(key)
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def head(self):
        # 取得第一个元素
        return self.values[0]

    def tail(self):
        # 取得除第一个元素外的所有元素
        return self.values[1:]

    def init(self):
        # 取得除最后一个元素外的所有元素
        return self.values[:-1]

    def last(self):
        # 取得最后一个元素
        return self.values[-1]

    def drop(self, n):
        # 取得除前n个元素外的所有元素
        return self.values[n:]

    def take(self, n):
        # 取得前n个元素
        return self.values[:n]

    def __str__(self):
        return str(self.values)

    def __missing__(self, key):
        print('missing')
        if isinstance(key,int):
            raise KeyError('键值不存在')
        else:
            raise TypeError('键值类型错误')

    def keys(self):
        return self.values.keys()

    def __instancecheck__(self, instance):
        """
        判断一个实例是否是一个类的实例
        :param instance:
        :return:
        """
        return isinstance(instance,FunctionalList)

    def __subclasscheck__(self, subclass):
        """
        检查一个子类是否是一个类的子类
        :param subclass:
        :return:
        """
        return subclass(subclass,FunctionalList)

# 检查实例是否是类的实例

s = FunctionalList(['L'])
if isinstance(s,FunctionalList):
    print('yes')
else:
    print('no')

