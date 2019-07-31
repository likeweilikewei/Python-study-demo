#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
 如果属性查找（attribute lookup）在实例以及对应的类中（通过__dict__)失败， 那么会调用到类的__getattr__函数,
 如果没有定义这个函数，那么抛出AttributeError异常。由此可见，__getattr__一定是作用于属性查找的最后一步，兜底。
__setattr__(self,name,value)：如果要给 name 赋值，就调用这个方法。
__getattr__(self,name)：如果 name 被访问，同时它不存在的时候，此方法被调用。
__getattribute__(self,name)：当 name 被访问时自动被调用（注意：这个仅能用于新式类），无论 name 是否存在，都要被调用。
__delattr__(self,name)：如果要删除 name，这个方法就被调用。
"""


class Apple:
    def __init__(self,name,size):
        self.__name = name
        self.__size = size
        super(Apple, self).__setattr__('counter', 0)

    def __getattr__(self, item):
        print('use getattr')
        return '---------------------------------'

    def __setattr__(self, key, value):
        print('use setattr')
        self.__dict__[key] = 'apple-{}'.format(value)
        print(self.__dict__)

    def __repr__(self):
        print('use repr')
        return 'name:{},size:{}'.format(self.__name,self.__size)

    def __getattribute__(self, item):
        """
        除了赋值直接进__setattr__外，其他的任何属性和函数的访问都会 先 到这里，如果有这个属性就会进入访问，如果没有就会扔给兜底的__getattr__
        赋值的时候不能用self.xx = xx,要用self.__dict__[xx] = xx,否则会导致死循环。在用self.__dict__[xx]的时候会访问__getattribute__，因此__getattribute__
        里面不能用self.__dict__[xx]，否则会导致死循环，要用超类的__getattribute__访问：super().__getattribute__(item)。
        :return:
        """
        print('use getattribute.')
        # return self.__dict__[item]
        # 前者访问self.__dict__，只要访问这个属性，就要调用`getattribute``，这样就导致了无线递归下去（死循环）。要避免之。
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # print(super(Apple))
        # print(type(super(Apple)))
        # print(super(Apple,self))
        # print(type(super(Apple,self)))
        # print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        # return super(Apple,self).__getattribute__(item)
        # Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
        """
        super() 函数是用于调用父类(超类)的一个方法。
        super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。
        MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。
        """
        return super().__getattribute__(item)

    def __delattr__(self, item):
        """
        删除类的属性,可以直接删除，也可以用父类的delattr方法访问

        这个魔法方法和 __setattr__ 几乎相同，只不过它是用于处理删除属性时的行为。和 _setattr__ 一样，
        使用它时也需要多加小心，防止产生无限递归（在 __delattr__ 的实现中调用 del self.name 会导致无限递归）。
        :param item:
        :return:
        """
        # 每个self.counter都会使用getattribute，但是调用父类的__setattr__和__delattr__都不会使用getattribute
        print('use delattr')
        print(self.__dict__)
        # del self.__dict__[item]
        if item == 'price':
            super(Apple, self).__setattr__('counter', self.counter + 1)
        # if item == 'price':
        #     self.counter = self.counter + 1
        super(Apple, self).__delattr__(item)
        print(self.__dict__)

    def show(self):
        print(self.s,self.price,self.counter)

apple = Apple('a','20')
print(apple)
apple.show()
apple.price = 10
apple.show()
del apple.price
# show本身会调用getattribute
apple.show()

"""
输出：
use setattr
use getattribute.
use getattribute.
{'_Apple__name': 'apple-a'}
use setattr
use getattribute.
use getattribute.
{'_Apple__name': 'apple-a', '_Apple__size': 'apple-20'}
use repr
use getattribute.
use getattribute.
name:apple-a,size:apple-20
use getattribute.
use getattribute.
use getattr
use getattribute.
use getattr
use getattribute.
--------------------------------- --------------------------------- 0
use setattr
use getattribute.
use getattribute.
{'_Apple__name': 'apple-a', '_Apple__size': 'apple-20', 'counter': 0, 'price': 'apple-10'}
use getattribute.
use getattribute.
use getattr
use getattribute.
use getattribute.
--------------------------------- apple-10 0
use delattr
use getattribute.
{'_Apple__name': 'apple-a', '_Apple__size': 'apple-20', 'counter': 0, 'price': 'apple-10'}
use getattribute.
use getattribute.
{'_Apple__name': 'apple-a', '_Apple__size': 'apple-20', 'counter': 1}
use getattribute.
use getattribute.
use getattr
use getattribute.
use getattr
use getattribute.
--------------------------------- --------------------------------- 1
"""
