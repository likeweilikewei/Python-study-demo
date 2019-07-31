#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
为什么我们要讲协议？因为在Python中实现自定义容器类型需要用到一些协议。首先，不可变容器类型有如下协议：想实现一个不可变容器，你需要定义 __len__ 和 __getitem__ (后面会具体说明）。可变容器的协议除了上面提到的两个方法之外，还需要定义 __setitem__ 和 __delitem__ 。最后，如果你想让你的对象可以迭代，你需要定义 __iter__ ，这个方法返回一个迭代器。迭代器必须遵守迭代器协议，需要定义 __iter__ （返回它自己）和 next 方法。



6.2、容器背后的魔法方法
__len__(self)

返回容器的长度，可变和不可变类型都需要实现。

__getitem__(self, key)

定义对容器中某一项使用 self[key] 的方式进行读取操作时的行为。这也是可变和不可变容器类型都需要实现的一个方法。它应该在键的类型错误式产生 TypeError 异常，同时在没有与键值相匹配的内容时产生 KeyError 异常。

__setitem__(self, key)

定义对容器中某一项使用 self[key] 的方式进行赋值操作时的行为。它是可变容器类型必须实现的一个方法，同样应该在合适的时候产生 KeyError 和 TypeError 异常。

__iter__(self, key)

它应该返回当前容器的一个迭代器。迭代器以一连串内容的形式返回，最常见的是使用 iter() 函数调用，以及在类似 for x in container: 的循环中被调用。迭代器是他们自己的对象，需要定义 __iter__ 方法并在其中返回自己。

__reversed__(self)

定义了对容器使用 reversed() 内建函数时的行为。它应该返回一个反转之后的序列。当你的序列类是有序时，类似列表和元组，再实现这个方法，

__contains__(self, item)

__contains__ 定义了使用 in 和 not in 进行成员测试时类的行为。你可能好奇为什么这个方法不是序列协议的一部分，原因是，如果 __contains__ 没有定义，Python就会迭代整个序列，如果找到了需要的一项就返回 True 。

__missing__(self ,key)

__missing__ 在字典的子类中使用，它定义了当试图访问一个字典中不存在的键时的行为（目前为止是指字典的实例，例如我有一个字典 d ， “george” 不是字典中的一个键，当试图访问 d[“george’] 时就会调用 d.__missing__(“george”) ）。
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

# 定义列表
# s = FunctionalList(values=['li','ke','wei'])
# print(s)
# x = reversed(s)
# for __i in x:
#     print(__i)
# print(len(s))
# print(s[1])

# 定义字典
# xs = FunctionalList(values={'li':1,'ke':2})
# print(xs['lis'])
# print(xs.keys())
# if 'li' in xs.keys():
#     print('yes')
# else:
#     print('no')

# 定义元组
xx = FunctionalList(values=['li','ke','wei'])
print(xx)
print(xx['j'])
