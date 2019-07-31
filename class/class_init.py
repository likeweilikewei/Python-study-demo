#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_1():
    """
    AttributeError: 'B' object has no attribute 'namea'
    在子类中，构造函数被重写，但新的构造方法没有任何关于初始化父类的namea属性的代码，为了达到预期的效果，
    子类的构造方法必须调用其父类的构造方法来进行基本的初始化。有两种方法能达到这个目的：调用超类构造方法的未绑定版本，
    或者使用super函数。
    如果子类和父类都有构造函数，子类其实是重写了父类的构造函数，如果不显式调用父类构造函数，
    父类的构造函数就不会被执行，导致子类实例访问父类初始化方法中初始的变量就会出现问题。
    :return:
    """
    class A:
        def __init__(self):
            self.namea = "aaa"

        def funca(self):
            print("function a : %s" % self.namea)

    class B(A):
        def __init__(self):
            self.nameb = "bbb"

        def funcb(self):
            print("function b : %s" % self.nameb)

    b = B()
    print(b.nameb)
    b.funcb()

    b.funca()


def test_2():
    """
    方法一：调用未绑定的超类构造方法
    这种方法叫做调用父类的未绑定的构造方法。在调用一个实例的方法时，该方法的self参数会被自动绑定到实例上
    （称为绑定方法）。但如果直接调用类的方法（比如A.__init），那么就没有实例会被绑定。
    这样就可以自由的提供需要的self参数，这种方法称为未绑定unbound方法。
    通过将当前的实例作为self参数提供给未绑定方法，B类就能使用其父类构造方法的所有实现，从而namea变量被设置。
    """
    class A:
        def __init__(self):
            self.namea = "aaa"

        def funca(self):
            print("function a : %s" % self.namea)

    class B(A):
        def __init__(self):
            # 这一行解决了问题
            A.__init__(self)
            self.nameb = "bbb"

        def funcb(self):
            print("function b : %s" % self.nameb)

    b = B()
    print(b.nameb)
    b.funcb()
    b.funca()


def test_3():
    """
    方法二：使用super函数
    如上有注释的为新增的代码，其中第一句让类A继承自object类，这样才能使用super函数，
    因为这是python的“新式类”支持的特性。当前的雷和对象可以作为super函数的参数使用，
    调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法。
    super函数会返回一个super对象，这个对象负责进行方法解析，解析过程其会自动查找所有的父类以及父类的父类。
    方法一更直观，方法二可以一次初始化所有超类
    super函数比在超累中直接调用未绑定方法更直观，但是其最大的有点是如果子类继承了多个父类，
    它只需要使用一次super函数就可以。然而如果没有这个需求，直接使用A.__init__(self)更直观一些。

    第二方法，在python3中父类A可以不继承object，因为python3中类都是默认继承object的：
    其中super的参数可以省略，代码简化为：

    在子类中初始化重名的参数也是可以初始化父类的
    :return:
    """
    # 父类需要继承object对象
    class A(object):
        def __init__(self, x):
            self.namea = "aaa"
            self.x = x

        def funca(self):
            print("function a : %s" % self.namea)

        def funcx(self):
            print('function x : {}'.format(self.x))

    class C(object):
        def __init__(self, z):
            self.z = z + 2

        def funcz(self):
            print('function z : {}'.format(self.z))

    class B(A, C):
        def __init__(self, x, y, z):
            # 这一行解决问题
            super(B, self).__init__(x=x)
            # super().__init__(x=x)
            self.z = z + 1  # 父类只会初始化这里的z+1
            self.nameb = "bbb"
            self.y = y

        def funcb(self):
            print("function b : %s" % self.nameb)

        def funcy(self):
            print('function y : {}'.format(self.y))

    b = B(x=666, y=888, z=999)
    print(b.nameb)
    b.funcb()
    b.funca()
    b.funcx()
    b.funcy()
    b.funcz()

# test_3()


def test_4():
    """
    多重继承一般用方法一进行初始化
    :return:
    """
    class A(object):
        def __init__(self, a):
            print('__init__ A', str(a))
            self.A = a

    class B(A):
        def __init__(self, a, b):
            A.__init__(self, a+1)  # 修改此处，不知道为什么super(B, self).__init__(a)会有问题
            print('__init__ B', str(b))
            self.B = b

    class C(A):
        def __init__(self, a, c):
            A.__init__(self, a+3)  # 修改此处， 不知道为什么super(C, self).__init__(a)会有问题
            print('__init__ C', str(c))
            self.C = c

    class D(B, C):
        def __init__(self, a, b, c, d):
            B.__init__(self, a, b)  # 这行及下行代码有问题，貌似对基类A进行了两次初始化
            C.__init__(self, a, c)
            print('__init__ D', str(d))
            self.D = d

    shanghe = D(1, 2, 3, 4)

test_4()
