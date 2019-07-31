#! /usr/bin/env python
# -*- coding=utf-8 -*-

import math

"""
就像你可以使用比较操作符来比较类的实例，你也可以定义数值操作符的行为。
固定好你的安全带，这样的操作符真的有很多。看在组织的份上，我把它们分成了五类：一元操作符，
常见算数操作符，反射算数操作符（后面会涉及更多），增强赋值操作符，和类型转换操作符。
"""


class Apple0:
    """
    一元操作符
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __pos__(self):
        """
        取正操作，没什么用
        :return:
        """
        self.size = +self.size

    def __neg__(self):
        """
        取负操作
        :return:
        """
        self.size = -self.size

    def __str__(self):
        return '{}'.format(self.size)

    def __abs__(self):
        """
        取绝对值
        :return:
        """
        self.size = abs(self.size)

    def __invert__(self):
        """
        按位取反，相当于~x = -x - 1
        只能针对指数
        :return:
        """
        if isinstance(self.size,int):
            self.size = ~self.size

    def __round__(self, n=None):
        """
        四舍五入
        实现内建函数 round() ，n 是近似小数点的位数。
        :param n:
        :return:
        """
        self.size = round(self.size,n)

    def __floor__(self):
        """
        向下取整
        实现内建函数 round() ，n 是近似小数点的位数。
        :return:
        """
        self.size = math.floor(self.size)

    def __ceil__(self):
        """
        实现 math.ceil() 函数，即向上取整。
        :return:
        """
        self.size = math.ceil(self.size)

    def __trunc__(self):
        """
        实现 math.trunc() 函数，即距离 零 最近的整数。
        :return:
        """
        self.size = math.trunc(self.size)

# apple0 = Apple0('li',-27.1345)
# -apple0
# print(apple0)
# -apple0
# print(apple0)
# print(apple0)
# abs(apple0)
# print(apple0)
# ~apple0
# print(apple0)
# round(apple0,3)
# print(apple0)

# 向下取整
# print(apple0)
# math.floor(apple0)
# print(apple0)

# 向上取整
# print(apple0)
# math.ceil(apple0)
# print(apple0)

# 得到最近的整数
# print(apple0)
# math.trunc(apple0)
# print(apple0)
# print(math.trunc(27.666))


class Apple1:
    """
    二元操作符
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __add__(self, other):
        """
        实现加法操作
        :param other:
        :return:
        """
        return self.size + other.size

    def __sub__(self, other):
        """
        实现减法操作
        :param other:
        :return:
        """
        return self.size - other.size

    def __str__(self):
        return '{}'.format(self.size)

    def __mul__(self, other):
        """
        实现乘法操作。
        :param other:
        :return:
        """
        # return self.size * other.size
        return Apple1(self.__name,self.size*other.size)

    def __floordiv__(self, other):
        """
        实现使用 // 操作符的整数除法。
        对结果向下取整
        :param other:
        :return:
        """
        # print('ys')
        return self.size // other.size

    def __divmod__(self, other):
        """
        python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
        :param other:
        :return:
        """
        return divmod(self.size,other.size)

    def __truediv__(self, other):
        """
        __div__ python3已经废除，实现除法,python2中的除法是整除
        :param other:
        :return:
        """
        return self.size / other.size

    def __mod__(self, other):
        """
        实现 % 取余操作。
        :param other:
        :return:
        """
        return self.size % other.size

    def __pow__(self, power, modulo=None):
        """
        实现 ** 操作符。
        :param power:
        :param modulo:
        :return:
        """
        return self.size ** power.size

    def __lshift__(self, other):
        """
        实现左移位运算符 << 。
        二进制左移
        :param other:
        :return:
        """
        return self.size << other.size

    def __rshift__(self, other):
        """
        实现右移运算符 >>
        :param other:
        :return:
        """
        return self.size >> other.size

    def __and__(self, other):
        """
        实现按位与运算符 & 。
        :param other:
        :return:
        """
        return self.size & other.size

    def __or__(self, other):
        """
        实现按位或运算符 | 。
        :param other:
        :return:
        """
        return self.size | other.size

    def __xor__(self, other):
        """
        实现按位异或运算符 ^ 。
        :param other:
        :return:
        """
        return self.size ^ other.size


# apple1 = Apple1('li',-27.1345)
# print(apple1)
#
# apple2 = Apple1('li',34)
# print(apple2)

# 加法操作
# result1 = apple2 + apple1
# print(result1)

# 减法操作
# result2 = apple1 - apple2
# print(result2)

# 乘法操作
# result3 = apple1 * apple2
# print(result3)
# print(type(result3))

# 整除
# result4 = apple1 // apple2
# print(result4)
# print(-35//34)

# 除数和余数运算结果结合起来
# result5 = divmod(apple1,apple2)
# print(result5)

# 除法
# result6 = apple1 / apple2
# print(result6)
# print(type(result6))

# 取余
# result7 = apple1 % apple2
# print(result7)
# print(type(result7))

# 幂方
# apple3 = Apple1('li',-27)
# print(apple3)
#
# apple4 = Apple1('li',34)
# print(apple4)
# result8 = apple3 ** apple4
# print(result8)
# print(type(result8))

# 左移运算符
# apple3 = Apple1('li',2)
# print(apple3)
#
# apple4 = Apple1('li',2)
# print(apple4)
# result9 = apple3 << apple4
# print(result9)
# print(10<<3)

# 右移运算符
# apple3 = Apple1('li',2)
# print(apple3)
#
# apple4 = Apple1('li',2)
# print(apple4)
# result9 = apple3 >> apple4
# print(result9)
# print(2>>2)

# 按位与
# apple3 = Apple1('li',2)
# print(apple3)
#
# apple4 = Apple1('li',3)
# print(apple4)
# result9 = apple3 & apple4
# print(result9)

# 按位或
# apple3 = Apple1('li',2)
# print(apple3)
#
# apple4 = Apple1('li',3)
# print(apple4)
# result9 = apple3 | apple4
# print(result9)

# 按位亦或
# apple3 = Apple1('li',2)
# print(apple3)
#
# apple4 = Apple1('li',3)
# print(apple4)
# result9 = apple3 ^ apple4
# print(result9)


class Apple2:
    """
    反射操作符
    这里有几点要注意的地方：

    1.不支持同一个类的实例进行反射运算：
    2.当一个类实现了__add__的时候，将会掩盖__radd__方法，也就是__add__的优先度更高：
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __radd__(self, other):
        """
        实现反射加法操作
        :param other:
        :return:
        """
        return 'Apple2 radd:{} + {} = {}'.format(self.size,other.size,self.size + other.size)

    def __rsub__(self, other):
        """
        实现减法操作
        :param other:
        :return:
        """
        return 'Apple2 rsub:{} - {} = {}'.format(self.size,other.size,self.size - other.size)

    def __str__(self):
        return '{}'.format(self.size)

    def __rmul__(self, other):
        """
        实现反射乘法操作。
        :param other:
        :return:
        """
        # return self.size * other.size
        # return Apple1(self.__name,self.size*other.size)
        return 'Apple2 rmul:{} * {} = {}'.format(self.size, other.size, self.size * other.size)

    def __rfloordiv__(self, other):
        """
        实现使用 // 反射操作符的整数除法。
        对结果向下取整
        :param other:
        :return:
        """
        # print('ys')
        return 'Apple2 rfloordiv:{} // {} = {}'.format(self.size, other.size, self.size // other.size)

    def __rdivmod__(self, other):
        """
        python rdivmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。反射版本
        :param other:
        :return:
        """
        return 'Apple2 divmod({},{}) = {}'.format(self.size, other.size, divmod(self.size,other.size))

    def __rtruediv__(self, other):
        """
        __div__ python3已经废除，实现除法,python2中的除法是整除,反射版本
        :param other:
        :return:
        """
        return 'Apple2 divmod({},{}) = {}'.format(self.size, other.size, self.size / other.size)

    def __rmod__(self, other):
        """
        实现 % 反射取余操作符。
        :param other:
        :return:
        """
        return 'Apple2 rmod({},{}) = {}'.format(self.size, other.size, self.size % other.size)

    def __rpow__(self, power, modulo=None):
        """
        实现 ** 反射操作符。
        :param power:
        :param modulo:
        :return:
        """
        return 'Apple2 rpow({},{}) = {}'.format(self.size, power.size, self.size ** power.size)

    def __rlshift__(self, other):
        """
        实现反射左移位运算符 << 的作用。
        二进制左移
        :param other:
        :return:
        """
        return 'Apple2 rlshift({},{}) = {}'.format(self.size, other.size, self.size << other.size)

    def __rshift__(self, other):
        """
        实现反射右移位运算符 >> 的作用。
        :param other:
        :return:
        """
        return 'Apple2 rshift({},{}) = {}'.format(self.size, other.size, self.size >> other.size)

    def __rand__(self, other):
        """
        实现反射按位与运算符 & 。
        :param other:
        :return:
        """
        return 'Apple2 rand({},{}) = {}'.format(self.size, other.size, self.size & other.size)

    def __ror__(self, other):
        """
        实现反射按位或运算符 | 。
        :param other:
        :return:
        """
        return 'Apple2 ror({},{}) = {}'.format(self.size, other.size, self.size | other.size)

    def __rxor__(self, other):
        """
        实现反射按位异或运算符 ^ 。
        :param other:
        :return:
        """
        return 'Apple2 ror({},{}) = {}'.format(self.size, other.size, self.size ^ other.size)


class Apple3:
    """
    反射操作符
    这里有几点要注意的地方：

    1.不支持同一个类的实例进行反射运算：
    2.当一个类实现了__add__的时候，将会掩盖__radd__方法，也就是__add__的优先度更高：
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __radd__(self, other):
        """
        实现反射加法操作
        当一个类实现了__add__的时候，将会掩盖__radd__方法，也就是__add__的优先度更高：
        当左边实例有__add__的时候就会使用__add__，否则使用__radd__来计算
        :param other:
        :return:
        """
        return 'Apple2 radd:{} + {} = {}'.format(self.size,other.size,self.size + other.size)

    def __rsub__(self, other):
        """
        实现减法操作
        :param other:
        :return:
        """
        return 'Apple2 rsub:{} - {} = {}'.format(self.size,other.size,self.size - other.size)

    def __str__(self):
        return '{}'.format(self.size)

    def __rmul__(self, other):
        """
        实现反射乘法操作。
        :param other:
        :return:
        """
        # return self.size * other.size
        # return Apple1(self.__name,self.size*other.size)
        return 'Apple2 rmul:{} * {} = {}'.format(self.size, other.size, self.size * other.size)

    def __rfloordiv__(self, other):
        """
        实现使用 // 反射操作符的整数除法。
        对结果向下取整
        :param other:
        :return:
        """
        # print('ys')
        return 'Apple2 rfloordiv:{} // {} = {}'.format(self.size, other.size, self.size // other.size)

    def __rdivmod__(self, other):
        """
        python rdivmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。反射版本
        :param other:
        :return:
        """
        return 'Apple2 divmod({},{}) = {}'.format(self.size, other.size, divmod(self.size,other.size))

    def __rtruediv__(self, other):
        """
        __div__ python3已经废除，实现除法,python2中的除法是整除,反射版本
        :param other:
        :return:
        """
        return 'Apple2 rtruediv({},{}) = {}'.format(self.size, other.size, self.size / other.size)

    def __rmod__(self, other):
        """
        实现 % 反射取余操作符。
        :param other:
        :return:
        """
        return 'Apple2 rmod({},{}) = {}'.format(self.size, other.size, self.size % other.size)

    def __rpow__(self, power, modulo=None):
        """
        实现 ** 反射操作符。
        :param power:
        :param modulo:
        :return:
        """
        return 'Apple2 rpow({},{}) = {}'.format(self.size, power.size, self.size ** power.size)

    def __rlshift__(self, other):
        """
        实现反射左移位运算符 << 的作用。
        二进制左移
        :param other:
        :return:
        """
        return 'Apple2 rlshift({},{}) = {}'.format(self.size, other.size, self.size << other.size)

    def __rshift__(self, other):
        """
        实现反射右移位运算符 >> 的作用。
        :param other:
        :return:
        """
        return 'Apple2 rshift({},{}) = {}'.format(self.size, other.size, self.size >> other.size)

    def __rand__(self, other):
        """
        实现反射按位与运算符 & 。
        :param other:
        :return:
        """
        return 'Apple2 rand({},{}) = {}'.format(self.size, other.size, self.size & other.size)

    def __ror__(self, other):
        """
        实现反射按位或运算符 | 。
        :param other:
        :return:
        """
        return 'Apple2 ror({},{}) = {}'.format(self.size, other.size, self.size | other.size)

    def __rxor__(self, other):
        """
        实现反射按位异或运算符 ^ 。
        :param other:
        :return:
        """
        return 'Apple2 ror({},{}) = {}'.format(self.size, other.size, self.size ^ other.size)

# apple1 = Apple2('li',-27.1345)
# print(apple1)
#
# apple2 = Apple3('li',34)
# print(apple2)

# 反射加法操作
# result1 = apple1 + apple2
# print(result1)

# 反射减法操作
# result2 = apple1 - apple2
# print(result2)

# 反射乘法操作
# result3 = apple1 * apple2
# print(result3)
# print(type(result3))

# 反射整除
# result4 = apple1 // apple2
# print(result4)
# print(-35//34)

# 反射除数和余数运算结果结合起来
# result5 = divmod(apple1,apple2)
# print(result5)

# 反射除法
# result6 = apple1 / apple2
# print(result6)
# print(type(result6))

# 反射取余
# result7 = apple1 % apple2
# print(result7)
# print(type(result7))

# 反射幂方
# apple3 = Apple2('li',-27)
# print(apple3)

# apple4 = Apple3('li',34)
# print(apple4)
# result8 = apple3 ** apple4
# print(result8)
# print(type(result8))

# 反射左移运算符
# apple3 = Apple2('li',2)
# print(apple3)
#
# apple4 = Apple3('li',3)
# print(apple4)
# result9 = apple3 << apple4
# print(result9)
# print(10<<3)

# 反射右移运算符
# apple3 = Apple2('li',6)
# print(apple3)
#
# apple4 = Apple3('li',2)
# print(apple4)
# result9 = apple3 >> apple4
# print(result9)
# print(2>>2)

# 反射按位与
# apple3 = Apple2('li',2)
# print(apple3)
#
# apple4 = Apple3('li',3)
# print(apple4)
# result9 = apple3 & apple4
# print(result9)
# #
# 反射按位或
# apple3 = Apple2('li',2)
# print(apple3)
#
# apple4 = Apple3('li',3)
# print(apple4)
# result9 = apple3 | apple4
# print(result9)
#
# 反射按位亦或
# apple3 = Apple2('li',2)
# print(apple3)
#
# apple4 = Apple3('li',3)
# print(apple4)
# result9 = apple3 ^ apple4
# print(result9)



class Apple4:
    """
    增强赋值操作符
    这里有几点要注意的地方：

    1.不支持同一个类的实例进行增强赋值运算：
    2.当一个类实现了__add__的时候，将会掩盖__iadd__方法，也就是__add__的优先度更高：
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __iadd__(self, other):
        """
        实现增强赋值加法操作
        :param other:
        :return:
        """
        # return 'Apple4 radd:{} + {} = {}'.format(self.size,other.size,self.size + other.size)
        return Apple4(self.__name,self.size + other.size)

    def __isub__(self, other):
        """
        实现减法操作
        :param other:
        :return:
        """
        return 'Apple4 rsub:{} - {} = {}'.format(self.size,other.size,self.size - other.size)

    def __str__(self):
        return '{}'.format(self.size)

    def __imul__(self, other):
        """
        实现增强赋值乘法操作。
        :param other:
        :return:
        """
        # return self.size * other.size
        # return Apple1(self.__name,self.size*other.size)
        return 'Apple4 rmul:{} * {} = {}'.format(self.size, other.size, self.size * other.size)

    def __ifloordiv__(self, other):
        """
        实现使用 // 增强赋值操作符的整数除法。
        对结果向下取整
        :param other:
        :return:
        """
        # print('ys')
        return 'Apple4 rfloordiv:{} // {} = {}'.format(self.size, other.size, self.size // other.size)

    def __idivmod__(self, other):
        """
        python rdivmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。增强赋值版本
        :param other:
        :return:
        """
        return 'Apple4 divmod({},{}) = {}'.format(self.size, other.size, divmod(self.size,other.size))

    def __itruediv__(self, other):
        """
        __div__ python3已经废除，实现除法,python2中的除法是整除,增强赋值版本
        :param other:
        :return:
        """
        return 'Apple4 divmod({},{}) = {}'.format(self.size, other.size, self.size / other.size)

    def __imod__(self, other):
        """
        实现 % 增强赋值取余操作符。
        :param other:
        :return:
        """
        return 'Apple4 rmod({},{}) = {}'.format(self.size, other.size, self.size % other.size)

    def __ipow__(self, power, modulo=None):
        """
        实现 ** 增强赋值操作符。
        :param power:
        :param modulo:
        :return:
        """
        return 'Apple4 rpow({},{}) = {}'.format(self.size, power.size, self.size ** power.size)

    def __ilshift__(self, other):
        """
        实现增强赋值左移位运算符 << 的作用。
        二进制左移
        :param other:
        :return:
        """
        return 'Apple4 rlshift({},{}) = {}'.format(self.size, other.size, self.size << other.size)

    def __ishift__(self, other):
        """
        实现增强赋值右移位运算符 >> 的作用。
        :param other:
        :return:
        """
        return 'Apple4 rshift({},{}) = {}'.format(self.size, other.size, self.size >> other.size)

    def __iand__(self, other):
        """
        实现增强赋值按位与运算符 & 。
        :param other:
        :return:
        """
        return 'Apple4 rand({},{}) = {}'.format(self.size, other.size, self.size & other.size)

    def __ior__(self, other):
        """
        实现增强赋值按位或运算符 | 。
        :param other:
        :return:
        """
        return 'Apple4 ror({},{}) = {}'.format(self.size, other.size, self.size | other.size)

    def __ixor__(self, other):
        """
        实现增强赋值按位异或运算符 ^ 。
        :param other:
        :return:
        """
        return 'Apple4 ror({},{}) = {}'.format(self.size, other.size, self.size ^ other.size)


class Apple5:
    """
    增强赋值操作符
    这里有几点要注意的地方：

    1.不支持同一个类的实例进行增强赋值运算：
    2.当一个类实现了__add__的时候，将会掩盖__iadd__方法，也就是__add__的优先度更高：
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __iadd__(self, other):
        """
        实现增强赋值加法操作
        当一个类实现了__add__的时候，将会掩盖__iadd__方法，也就是__add__的优先度更高：
        当左边实例有__add__的时候就会使用__add__，否则使用__iadd__来计算
        :param other:
        :return:
        """
        return 'Apple4 radd:{} + {} = {}'.format(self.size,other.size,self.size + other.size)

    def __isub__(self, other):
        """
        实现减法操作
        :param other:
        :return:
        """
        return 'Apple4 rsub:{} - {} = {}'.format(self.size,other.size,self.size - other.size)

    def __str__(self):
        return '{}'.format(self.size)

    def __imul__(self, other):
        """
        实现增强赋值乘法操作。
        :param other:
        :return:
        """
        # return self.size * other.size
        # return Apple1(self.__name,self.size*other.size)
        return 'Apple4 rmul:{} * {} = {}'.format(self.size, other.size, self.size * other.size)

    def __ifloordiv__(self, other):
        """
        实现使用 // 增强赋值操作符的整数除法。
        对结果向下取整
        :param other:
        :return:
        """
        # print('ys')
        return 'Apple4 rfloordiv:{} // {} = {}'.format(self.size, other.size, self.size // other.size)

    def __idivmod__(self, other):
        """
        python rdivmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。增强赋值版本
        :param other:
        :return:
        """
        return 'Apple4 divmod({},{}) = {}'.format(self.size, other.size, divmod(self.size,other.size))

    def __itruediv__(self, other):
        """
        __div__ python3已经废除，实现除法,python2中的除法是整除,增强赋值版本
        :param other:
        :return:
        """
        return 'Apple4 rtruediv({},{}) = {}'.format(self.size, other.size, self.size / other.size)

    def __imod__(self, other):
        """
        实现 % 增强赋值取余操作符。
        :param other:
        :return:
        """
        return 'Apple4 rmod({},{}) = {}'.format(self.size, other.size, self.size % other.size)

    def __ipow__(self, power, modulo=None):
        """
        实现 ** 增强赋值操作符。
        :param power:
        :param modulo:
        :return:
        """
        return 'Apple4 rpow({},{}) = {}'.format(self.size, power.size, self.size ** power.size)

    def __ilshift__(self, other):
        """
        实现增强赋值左移位运算符 << 的作用。
        二进制左移
        :param other:
        :return:
        """
        return 'Apple4 rlshift({},{}) = {}'.format(self.size, other.size, self.size << other.size)

    def __ishift__(self, other):
        """
        实现增强赋值右移位运算符 >> 的作用。
        :param other:
        :return:
        """
        return 'Apple4 rshift({},{}) = {}'.format(self.size, other.size, self.size >> other.size)

    def __iand__(self, other):
        """
        实现增强赋值按位与运算符 & 。
        :param other:
        :return:
        """
        return 'Apple4 rand({},{}) = {}'.format(self.size, other.size, self.size & other.size)

    def __ior__(self, other):
        """
        实现增强赋值按位或运算符 | 。
        :param other:
        :return:
        """
        return 'Apple4 ror({},{}) = {}'.format(self.size, other.size, self.size | other.size)

    def __ixor__(self, other):
        """
        实现增强赋值按位异或运算符 ^ 。
        :param other:
        :return:
        """
        return 'Apple4 ror({},{}) = {}'.format(self.size, other.size, self.size ^ other.size)

# apple1 = Apple4('li',-27.1345)
# print(apple1)
#
# apple2 = Apple5('li',34)
# print(apple2)
#
# # 增强赋值加法操作
# apple1 += apple2
# print(apple1)
# print(type(apple1))

# 增强赋值减法操作
# result2 = apple1 - apple2
# print(result2)

# 增强赋值乘法操作
# result3 = apple1 * apple2
# print(result3)
# print(type(result3))

# 增强赋值整除
# result4 = apple1 // apple2
# print(result4)
# print(-35//34)

# 增强赋值除数和余数运算结果结合起来
# result5 = divmod(apple1,apple2)
# print(result5)

# 增强赋值除法
# result6 = apple1 / apple2
# print(result6)
# print(type(result6))

# 增强赋值取余
# result7 = apple1 % apple2
# print(result7)
# print(type(result7))

# 增强赋值幂方
# apple3 = Apple4('li',-27)
# print(apple3)

# apple4 = Apple5('li',34)
# print(apple4)
# result8 = apple3 ** apple4
# print(result8)
# print(type(result8))

# 增强赋值左移运算符
# apple3 = Apple4('li',2)
# print(apple3)
#
# apple4 = Apple5('li',3)
# print(apple4)
# result9 = apple3 << apple4
# print(result9)
# print(10<<3)

# 增强赋值右移运算符
# apple3 = Apple4('li',6)
# print(apple3)
#
# apple4 = Apple5('li',2)
# print(apple4)
# result9 = apple3 >> apple4
# print(result9)
# print(2>>2)

# 增强赋值按位与
# apple3 = Apple4('li',2)
# print(apple3)
#
# apple4 = Apple5('li',3)
# print(apple4)
# result9 = apple3 & apple4
# print(result9)
# #
# 增强赋值按位或
# apple3 = Apple4('li',2)
# print(apple3)
#
# apple4 = Apple5('li',3)
# print(apple4)
# result9 = apple3 | apple4
# print(result9)
#
# 增强赋值按位亦或
# apple3 = Apple4('li',2)
# print(apple3)
#
# apple4 = Apple5('li',3)
# print(apple4)
# result9 = apple3 ^ apple4
# print(result9)


class Apple6:
    """
    类型转换操作符
    Python也有一系列的魔法方法用于实现类似 float() 的内建类型转换函数的操作。它们是这些：
    """
    def __init__(self,name,size):
        self.__name = name
        self.size = size

    def __int__(self):
        """
        实现到int的类型转换。
        :return:
        """
        self.size = int(self.size)
        return self.size

    def __str__(self):
        return '{}:{}'.format(self.size,type(self.size))

    def __long__(self):
        """"
         python3 彻底废弃了 long+int 双整数实现的方法, 统一为 int , 支持高精度整数运算.
        """
        pass

    def __float__(self):
        """
        实现到float的类型转换。
        :return:
        """
        self.size = float(self.size)
        return self.size

    def __complex__(self):
        """
        实现到complex的类型转换。负数类型
        :return:
        """
        self.size = complex(self.size)
        return self.size

    def __oct__(self):
        """
        实现到八进制数的类型转换。
        :return:
        """
        self.size = oct(int(self.size))
        return self.size

    def __hex__(self):
        """
        实现到十六进制数的类型转换。
        :return:
        """
        self.size = hex(int(self.size))

    def __index__(self):
        """
        实现当对象用于切片表达式时到一个整数的类型转换。如果你定义了一个可能会用于切片操作的数值类型，你应该定义 __index__。
        :return:
        """
        return int(self.size)

    def __trunc__(self):
        """
        实现 math.trunc() 函数，即距离 零 最近的整数。
        :return:
        """
        self.size = math.trunc(self.size)

    def __coerce__(self, other):
        """
        该方法用于实现混合模式算数运算，如果不能进行类型转换， __coerce__ 应该返回 None 。
        反之，它应该返回一个二元组 self 和 other ，这两者均已被转换成相同的类型。3.0废弃
        实现了类型的强制转换，这个方法对应于 coerce 内建函数的结果（python3.0开始去掉了此函数，也就是该魔法方法也没意义了，至于后续的版本是否重新加入支持，要视官方而定。）
        这个函数的作用是强制性地将两个不同的数字类型转换成为同一个类型，例如：
        #coerce(x, y) -> (x1, y1)
　　  方法返回一个元祖，分别对应转换后的两个数字。其优先级为：复数>浮点数>长整型>整型。在转换的时候，会转换为两个参数中优先级高的类型。当转换无法完成的时候，会触发 TypeError。
　　  而当我们定义这个魔法方法时，如果转换无法完成，应该返回None。
　　  这里有个重要的机制，当python进行运算的时候，如 1 + 1.0 时，会先调用 coerce 函数将其转换为同一个类型，然后再进行运行，这也就是为什么 1 + 1.0 = 2.0，因为转换之后实际进行的运算为 1.0 +1.0。得到这样的结果也就不奇怪了。
        :param other:
        :return:
        """
        pass



# int必须要有返回
# apple6 = Apple6(name='li',size=3.9)
# print(int(3.9))
# print(apple6)
# int(apple6)
# print(apple6)

# float
# apple6 = Apple6(name='li',size='3.4')
# print(apple6)
# float(apple6)
# print(apple6)

# complex
# apple6 = Apple6(name='li',size=2)
# print(apple6)
# complex(apple6)
# print(apple6)

# 八进制
# apple6 = Apple6(name='li',size=100)
# print(apple6)
# s = oct(apple6)
# print(s)
# print(oct(12))

# 十六进制
# apple6 = Apple6(name='li',size=20)
# print(apple6)
# s = hex(apple6)
# print(s)
# print(hex(20))

# 切片索引
# apple6 = Apple6(name='li',size=2)
# print(apple6)
# name = ['li','ke','wei']
# print(name[apple6])
