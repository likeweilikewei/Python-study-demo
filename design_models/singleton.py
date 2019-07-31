#!/usr/bin/python
# coding:utf8

'''
Singleton

5.1. 模式动机
对于系统中的某些类来说，只有一个实例很重要，例如，一个系统中可以存在多个打印任务，
但是只能有一个正在工作的任务；一个系统只能有一个窗口管理器或文件系统；
一个系统只能有一个计时工具或ID（序号）生成器。

如何保证一个类只有一个实例并且这个实例易于被访问呢？定义一个全局变量可以确保对象随时都可以被访问，
但不能防止我们实例化多个对象。

一个更好的解决办法是让类自身负责保存它的唯一实例。这个类可以保证没有其他实例被创建，
并且它可以提供一个访问该实例的方法。这就是单例模式的模式动机。

5.2. 模式定义
单例模式(Singleton Pattern)：单例模式确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，
这个类称为单例类，它提供全局访问的方法。

单例模式的要点有三个：一是某个类只能有一个实例；二是它必须自行创建这个实例；
三是它必须自行向整个系统提供这个实例。单例模式是一种对象创建型模式。单例模式又名单件模式或单态模式。
'''
#use  __doc__ 属性


class Singleton(object):
    ''' A python style singleton '''

    def __new__(cls, *args, **kw):
        'new.'
        print(cls.__dict__)
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print(id(s1), s1)
    s2 = SingleSpam('spa')
    print(id(s2), s2)
    print(id(s1), s1)
    # 模块本身是一个对象，而每个对象都会有一个__doc__属性。该属性用于描述该对象的作用。
    print(Singleton.__doc__)
