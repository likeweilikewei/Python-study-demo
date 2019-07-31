#coding=utf-8


class Apple:
    """
    类的表示使用字符串来表示类是一个相当有用的特性。
    在Python中有一些内建方法可以返回类的表示，相对应的，
    也有一系列魔法方法可以用来自定义在使用这些内建函数时类的行为。
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __str__(self):
        """
        定义对类的实例调用 str() 时的行为。
        会覆盖repr
        :return:
        """
        print('str')
        return '{}:{}'.format(self.size,type(self.size))

    def __repr__(self):
        """
        定义对类的实例调用 repr() 时的行为。 str() 和 repr() 最主要的差别在于“目标用户”。
        repr() 的作用是产生机器可读的输出（大部分情况下，其输出可以作为有效的Python代码），
        而 str() 则产生人类可读的输出。
        :return:
        """
        print('repr')
        return '{}:{}'.format(self.size,type(self.size))

    def __unicode__(self):
        """
        python3使用__str__
        定义对类的实例调用 unicode() 时的行为。 unicode() 和 str() 很像，只是它返回unicode字符串。
        注意，如果调用者试图调用 str() 而你的类只实现了 __unicode__() ，那么类将不能正常工作。
        所有你应该总是定义 __str__() ，以防有些人没有闲情雅致来使用unicode。
        :return:
        """
        return '{}:{}'.format(self.size,type(self.size))

    def __format__(self, format_spec):
        """
        定义当类的实例用于新式字符串格式化时的行为，
        例如， “Hello, 0:abc!”.format(a) 会导致调用 a.__format__(“abc”) 。
        当定义你自己的数值类型或字符串类型时，你可能想提供某些特殊的格式化选项，
        这种情况下这个魔法方法会非常有用。
        :param format_spec:
        :return:
        """
        return str(self.size)

    def __hash__(self):
        """
        定义对类的实例调用 hash() 时的行为。它必须返回一个整数，其结果会被用于字典中键的快速比较。
        同时注意一点，实现这个魔法方法通常也需要实现 __eq__ ，并且遵守如下的规则：
        a == b 意味着 hash(a) == hash(b)。
        :return:
        """
        return int(self.size)

    def __bool__(self):
        """
        PYTHON2中叫__nonzero__
        类的__nonzero__方法用于将类转换为布尔值。通常在用类进行判断和将类转换成布尔值时调用。
        比如语句if A: print 'foo'中就会调用A.__nonzero__()来判断。
        下面这个程序应该能帮助你理解__nonzero__的作用。
        :return:
        """
        if int(self.size) > 0:
            return True
        else:
            return False

    def __dir__(self):
        """
        定义对类的实例调用 dir() 时的行为，这个方法应该向调用者返回一个属性列表。一般来说，没必要自己实现 __dir__ 。
        但是如果你重定义了 __getattr__ 或者 __getattribute__
        （下个部分会介绍），乃至使用动态生成的属性，以实现类的交互式使用，那么这个魔法方法是必不可少的。
        :return:
        """
        return [self.say]

    def say(self):
        print(self.size)

apple = Apple('LI',2)
print(apple)
s = format(apple)
print(s,type(s))

# hash
# print('---------------------------------')
# print(hash(apple))
# print(id(apple)/16)
# print(hash(2))
# print(hash(2)==hash(apple))
# print(hash(2) is hash(apple))
# print(2 is apple)
# print(id(2))
# print(id(apple))
# print(hash(2))
# a = 10
# print(hash(a))
# print(id(a))
# print(id(a)/16)

# bool
# apple1 = Apple('likewei',1)
# if apple1:
#     print('yes')
# else:
#     print('no')

# dir
#
# apples = Apple('li',189)
# print(dir(apples))
