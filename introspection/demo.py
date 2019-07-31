# coding: UTF-8
import sys  # 模块，sys指向这个模块对象
import inspect

"""
有时候我们会碰到这样的需求，需要执行对象的某个方法，或是需要对对象的某个字段赋值，而方法名或是字段名在编码代码时并不能确定，
需要通过参数传递字符串的形式输入。举个具体的例子：当我们需要实现一个通用的DBM框架时，可能需要对数据对象的字段赋值，
但我们无法预知用到这个框架的数据对象都有些什么字段，换言之，我们在写框架的时候需要通过某种机制访问未知的属性。

这个机制被称为反射（反过来让对象告诉我们他是什么），或是自省（让对象自己告诉我们他是什么，好吧我承认括号里是我瞎掰的- -#），
用于实现在运行时获取未知对象的信息。反射是个很吓唬人的名词，听起来高深莫测，在一般的编程语言里反射相对其他概念来说稍显复杂，
一般来说都是作为高级主题来讲；但在Python中反射非常简单，用起来几乎感觉不到与其他的代码有区别，
使用反射获取到的函数和方法可以像平常一样加上括号直接调用，获取到类后可以直接构造实例；不过获取到的字段不能直接赋值，
因为拿到的其实是另一个指向同一个地方的引用，赋值只能改变当前的这个引用而已。

dir([obj]): 
调用这个方法将返回包含obj大多数属性名的列表（会有一些特殊的属性不包含在内）。obj的默认值是当前的模块对象。
hasattr(obj, attr): 
这个方法用于检查obj是否有一个名为attr的值的属性，返回一个布尔值。
getattr(obj, attr): 
调用这个方法将返回obj中名为attr值的属性的值，例如如果attr为'bar'，则返回obj.bar。
setattr(obj, attr, val): 
调用这个方法将给obj的名为attr的值的属性赋值为val。例如如果attr为'bar'，则相当于obj.bar = val。
"""


def foo(): pass  # 函数，foo指向这个函数对象


class Cat(object):  # 类，Cat指向这个类对象
    def __init__(self, name='kitty'):
        self.name = name

    def sayHi(self):  # 实例方法，sayHi指向这个方法对象，使用类或实例.sayHi访问
        print(self.name, 'says Hi!')  # 访问名为name的字段，使用实例.name访问)


cat = Cat()
# cat是Cat类的实例对象

print(Cat.sayHi)  # 使用类名访问实例方法时，方法是未绑定的(unbound))
print(cat.sayHi)  # 使用实例访问实例方法时，方法是绑定的(bound)

cat = Cat('kitty')

print(cat.name)  # 访问实例属性
cat.sayHi()  # 调用实例方法

print(dir(cat))  # 获取实例的属性名，以列表形式返回
if hasattr(cat, 'name'):  # 检查实例是否有这个属性
    setattr(cat, 'name', 'tiger')  # same as: a.name = 'tiger'
print(getattr(cat, 'name'))  # same as: print a.name

getattr(cat, 'sayHi')()  # same as: cat.sayHi()
