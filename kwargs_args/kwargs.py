#! /user/bin/env python
# -*- coding=utf-8 -*-


def foo(x, **kwargs):
    """
    **kwargs：（表示的就是形参中按照关键字传值把多余的传值以字典的方式呈现）
    :param x:
    :param kwargs:
    :return:
    """
    print(x)
    print(kwargs)
# foo(1, y=1, a=2, b=3, c=4)  # 将y=1,a=2,b=3,c=4以字典的方式给了kwargs


def foo(x, *args, **kwargs):
    """
    关于**kwargs与位置参数、*args、默认参数混着用的问题：（注意顺序）
    位置参数、*args、**kwargs三者的顺序必须是位置参数、*args、**kwargs，不然就会报错
    :param x:
    :param args:
    :param kwargs:
    :return:
    """
    print(x)
    print(args)
    print(kwargs)
# foo(1, 2, 3, 4, y=1, a=2, b=3, c=4)  # 将1传给了x，将2,3,4以元组方式传给了args，y=1,a=2,b=3,c=4以字典的方式给了kwargs


def foo(x, y=1, **kwargs):
    """
    位置参数、默认参数、**kwargs三者的顺序必须是位置参数、默认参数、**kwargs，不然就会报错
    总之**kwargs总会在最后，不然报错
    :param x:
    :param y:
    :param kwargs:
    :return:
    """
    print(x)
    print(y)
    print(kwargs)
# foo(1, a=2, b=3, c=4)  # 将1按照位置传值给x，y按照默认参数为1，a=2,b=3,c=4以字典的方式给了kwargs


def foo(a, b, c, d):
    """
    **可以将参数以字典的形式传入
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    print(a)
    print(b)
    print(c)
    print(d)
# foo(**{"a": 2, "b": 3, "c": 4, "d": 5})  # **{"a":2,"b":3,"c":4,"d":5}是将字典里的每个值按照关键字传值的方式传给a,b,c,d


class Test:
    """
    **kwargs在函数里面的时候可以从外面传
    func(a=10,b=20)#这种函数在使用时必须指定参数值，使用key=value这种形式进行传播
    当函数里面是位置参数、默认参数、**kwargs类似的时候可以从外面用解析字典的形式进行传参
    """
    def __init__(self, _sex, name='li kewei', **kwargs):
        self.height = kwargs['height']
        self.name = name
        self.sex = _sex
        self.wedding = kwargs['wedding']

    def test(self):
        print(self.height)
        print(self.name)
        print(self.sex)
        print(self.wedding)
# params = {'height': 180, 'names': 'li kewei', 'wedding': 'no'}
# tests = Test('boy', name='like', **params)
# tests.test()


def test_2(__s1=2):
    """
    字典从其他函数返回的也可以传参
    最好不要用双下划线作为参数，在字典传参时候会失败，但是位置参数传参不会失败
    :return:
    """
    print(__s1)
    __s = 1
    return {'height': 180, 'name': 'li kewei', 'wedding': 'no', '_sex': 'girl'}, __s
params, test_result = test_2(__s1=3)
print(type(test_result))
testss = Test(**params)
testss.test()
