#! /usr/bin/env python
# -*-coding=utf-8-*-

"""
述符还有其他用处，如格式检查，类型检查，设置只读变量等。
设置一个只读变量的话，只要不让变量再赋值就好了，即调用__set__()函数时触发异常即可
"""


class descriptor(object):
    def __init__(self,val):
        self.val = val

    def __get__(self, obj,type = None):
        return self.val

    def __set__(self, obj, value):
        raise Exception('read only')


class Foo(object):
    d = descriptor(1)

d = Foo()
print(d.d)  # 1
d.d = 2    # 触发异常,read only
