#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_4():
    """
    多重继承一般用方法一进行初始化
    :return:
    """
    class A(object):
        def __init__(self, __a):
            print('__init__ A', str(__a))
            self.A = __a

    class B(A):
        def __init__(self, __a, b):
            __a = __a + 1
            A.__init__(self, __a)  # 修改此处，不知道为什么super(B, self).__init__(a)会有问题
            print('__init__ B', str(b))
            self.B = b

    class C(A):
        def __init__(self, __a, c):
            A.__init__(self, __a+3)  # 修改此处， 不知道为什么super(C, self).__init__(a)会有问题
            print('__init__ C', str(c))
            self.C = c

    class D(B, C):
        def __init__(self, __a, b, c, d):
            B.__init__(self, __a, b)  # 这行及下行代码有问题，貌似对基类A进行了两次初始化
            C.__init__(self, __a, c)
            print('__init__ D', str(d))
            self.D = d
    a = 3
    b = 2
    c = 3
    d = 4
    """
    不能显示的用__a = a
    使用相同变量名，无论是不是加下划线都会报同名问题
    属性前的双下划线是为了解决私有属性冲突
    """
    shanghe = D(a, b=b, c=c, d=d)
# test_4()


def test_5():
    """
    在Python中，没有类似 private 之类的关键字来声明私有方法或属性。
    Python中要声明私有属性，需要在属性前加上双下划线（但是结尾处不能有双下划线），
    如：self.__a。然而这样的什么方式并不是真正私有，而是“伪私有”。
    Python的伪私有属性，实际是通过变量名压缩（mangling）来实现变量名局部化。
    变量名压缩的规则：在初始的变量名头部加上一个下划线，再加上类的名称，最后是初始变量名的名称。
    :return:
    """
    class A(object):
        def __func(self): pass
    print(A.__dict__)
# test_5()


def test_6():
    """
    运行后出现异常，提示A没有属性__func，从而实现类似私有属性的功能。
    AttributeError: 'A' object has no attribute '__func'
    :return:
    """
    class A(object):
        def __func(self): pass

    if __name__ == '__main__':
        a = A()
        a.__func()
# test_6()


def test_7():
    """
    运行结果正常， 成功打印“Hello Python”字符串。
    Hello Python
    所以，Python的类并不存在正在的私有属性，通过双下划线实现的伪私有属性，
    本质上是对变量名进行压缩，使之无法直接在外部调用。
    :return:
    """
    class A(object):
        def __func(self): print('Hello Python')

    a = A()
    a._A__func()
# test_7()


def test_8():
    """
    从运行结果可以看出，每次 print(self.x)的内容，取决于 self.x 最后一次赋值的内容。
    Hello Python
    Hello Python
    在示例代码中，先调用 c3.meth1() 进行赋值，self.x的值为“Hello World”，再调用 c3.meth3() 进行赋值时，
    self.x的值被覆盖，目前的值为“Hello Python”。
    后续再调用c3.meth2()打印self.x的值时，实际上打印的是最后一次赋值结果，这在有些情况下跟类的设计初衷是相违背的：
    在C1中，meth2希望打印的是在meth1中赋值的内容：“Hello World”。
    :return:
    """
    class C1():
        def meth1(self):
            self.x = 'Hello World'

        def meth2(self):
            print(self.x)

    class C2():
        def meth3(self):
            self.x = 'Hello Python'

        def meth4(self):
            print(self.x)

    class C3(C1, C2):
        pass

    c3 = C3()
    c3.meth1()
    c3.meth3()
    c3.meth2()
    c3.meth4()
# test_8()


def test_9():
    """
    在使用伪私有属性后可以解决变量名self.x相互覆盖的问题（因为self.__x 被压缩成了 self._C1__x 和
    self._C2__x，变量名不同，不会互相覆盖）
    运行结果符合C1的设计初衷:调用meth2时应该打印出meth1的赋值结果：
    Hello World
    Hello Python
    :return:
    """
    class C1():
        def meth1(self):
            self.__x = 'Hello World'

        def meth2(self):
            print(self.__x)

    class C2():
        def meth3(self):
            self.__x = 'Hello Python'

        def meth4(self):
            print(self.__x)

    class C3(C1, C2):
        pass

    c3 = C3()
    c3.meth1()
    c3.meth3()
    c3.meth2()
    c3.meth4()
test_9()

"""
函数参数不要用前缀双下划线，因为类和参数会加类名前缀，导致传参错误
"""