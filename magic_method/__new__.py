#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
python中有二个特殊的方法__new__ 和 __init__ 方法。听黄哥来讲解。
__init__ 方法为初始化方法, __new__方法才是真正的构造函数。

1、__new__方法默认返回实例对象供__init__方法、实例方法使用。

Python中的__new__方法是对象实例化时调用的第一个方法，该方法仅读取一个cls参数后再把其他参数都传给用于指明对象初始化行为的__init__方法，也就是说我们可以在一个对象初始化之前进行其他操作，比如检查是否合法等；而另一个方法__del__可以用来销毁对象，定义了对象被垃圾回收的行为，我们可以利用该方法进行资源回收等操作。

我们可以通过重写__new__方法实现一个单例模式，在每次实例化之前检查该对象是否有已有实例。

1、self表示一个具体的实例本身。如果用了staticmethod，那么就可以无视这个self，将这个方法当成一个普通的函数使用。
2、cls表示这个类本身。

先调用__new__方法，返回该类的实例对象，这个实例对象就是__init__方法的第一个参数self，即self是__new__的返回值。

事实上，__str__是被print函数调用的，一般都是return一个什么东西。这个东西应该是以字符串的形式表现的。如果不是要用str()函数转换。
当你打印一个类的时候，那么print首先调用的就是类里面的定义的__str__
"""


class RedisManager:
    """生成redis连接池"""
    # new里面的参数不能少于init，但是init可以选择性取参数
    def __new__(cls,*args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(RedisManager, cls).__new__(cls)
        # print(cls._instance)
        # 这个地方打印 name会出错，因为此时还没有初始化，没有name属性
        # print("new args:{},kwargs:{}".format(args, kwargs))
        return cls._instance

    def __init__(self,*args,**kwargs):
        self.name = 'like'
        print(self)
        print("init args:{},kwargs:{}".format(args,kwargs))
        # print(a)

    def __str__(self):
        """
        str
        :return:方法 __str__ 应返回字符串，而不是打印。
        """
        # print('{}'.format('llsnl'))
        return '{}'.format(self.name)

a = RedisManager(2,b=1)
print(a)
