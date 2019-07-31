#! /user/bin/env python
# -*- coding=utf-8 -*-


"""
先来看看书上对于四个内置方法的描述：

​ __getattribute__(self, name): 当特性name被访问时自动被调用（只能在新式类中使用）

​ __getattr__(self, name): 当特性被访问且对象没有相应的特性时被自动调用

​ __setattr__(self, name, value): 当试图给特性name赋值时会被自动调用

​ __delattr__(self, name): 当试图删除特性name时被自动调用
重写这几个方法可以拦截对象的所有特性访问
"""


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, name, value):
        print('set attr', name, value)
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value

    def __getattr__(self, name):
        print('get attr', name)
        if name == 'size':
            return self.width, self.height
        else:
            print('No such attribute!!')
            raise AttributeError

a = Rectangle()
print(a.size)
a.size = 5, 6
print(a.size)
a.aa

"""
结果
set attr width 0
set attr height 0
get attr size
(0, 0)
set attr size (5, 6)
set attr width 5
set attr height 6
get attr size
(5, 6)
get attr aa
No such attribute!!
Traceback (most recent call last):
AttributeError

首先，创建了一个Rectangle对象的实例a。在实例a的初始化中，产生了两个暂未绑定（或者说暂时不存在）的特性width与height并对两者赋值。这个时候，实例调用了setattr()分别对width和height赋值，赋值方法是绑定到实例的dict之中（这就是python的赋值方法）。这里使用dict的原因是，如果使用一般的赋值方法，则会再一次调用setattr()方法，导致进入死循环

初始化完毕之后，尝试访问实例a中的size特性。由于a中并没有size特性，所以调用了getattr()方法

之后尝试使用size对实例a中的width和height捆绑赋值（类似于实现property函数那种），size调用一次setattr()方法，其中width和height又分别调用了一次setattr()方法

之后再一次尝试访问size特性

最后尝试访问实例a中的aa特性，这次直接抛出特性异常

如果我在此基础上重写__attribute__()方法呢？

这里有一个需要注意的地方，__attribute__()方法会拦截所有特性的访问，也就是说，对于保存特性的内置dict也会同样拦截

还有一个问题，如果调用了实例中没有的特性，是先调用getattr()方法还是getattribute()方法？

重新写了一段代码进行实验
"""


class Rectangle:
    def __init__(self):
        self.width = 1
        self.height = 2

    def __setattr__(self, name, value):
        print('set attr', name, value)
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value
            #super(Rectangle, self).__setattr__(name, value)

    def __getattr__(self, name):
        print('trying getting attr %s...' % name)
        if name == 'size':
            return self.width, self.height
        else:
            print('No such attr!')
            raise AttributeError

    def __getattribute__(self, name):
        print('get attribute', name)
        return super(Rectangle, self).__getattribute__(name)

    def __delattr__(self, name):
        print('del attr', name)
        if name == 'size':
            del self.width
            del self.height
        else:
            super(Rectangle, self).__delattr__(name)
a = Rectangle()
a.size = 5, 6
print(a.size)
a.aa

"""
结果
set attr width 1
get attribute __dict__
set attr height 2
get attribute __dict__
set attr size (5, 6)
set attr width 5
get attribute __dict__
set attr height 6
get attribute __dict__
get attribute size
trying getting attr size...
get attribute width
get attribute height
(5, 6)
get attribute aa
trying getting attr aa...
No such attr!
Traceback (most recent call last):
    raise AttributeError
AttributeError


同样，首先创建了一个Rectangle的实例a。在初始化的过程中，
产生了两个暂未绑定（或者说暂时不存在）的特性width与height并对两者赋值。
在赋值过程中，由于访问了两次dict，所以调用了两次getattribute()方法。
在getattribute()方法中，我直接使用super函数返回了超类的getattribute()方法，
全盘交给超类去做，我只是把方法拦截下来试验记录。

初始化之后使用size进行捆绑赋值也是类似

接下来我尝试访问不存在的size特性。发现首先调用的是getattribute()方法，之后调用了getattr()方法。
可以知道，在对特性的访问之中，首先调用的是getattribute()方法，若不存在，则再调用getattr()方法
"""
