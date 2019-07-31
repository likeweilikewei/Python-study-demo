#! /usr/bin/env python
# -*-coding=utf-8-*-

"""
中缀表达式转后缀表达式：
假定有中缀表达式1 + (( 2 + 3)* 4 ) – 5，请将它转化为后缀表达式。
方法一：利用表达式树
首先将中缀表达式转换为表达式树，然后后序遍历表达式树，所得结果就是后缀表达式。
将中缀表达式转化为表达式树方法：表达式树的树叶是操作数，而其他的节点为操作符，
根节点为优先级最低且靠右的操作符（如上述表达式优先级最低的是- 和+，但 + 更靠右，所以根为+），圆括号不包括。
"""

import queue
import copy


class Prototype:
    """
    原型，实现类的复制，复制优于创建
    """
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Queue:
    """
    queue
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(0)

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def data(self):
        return self.items


class Stack:
    """
    stack
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size()-1]


prototype = Prototype()
prototype.register_object(name='queue',obj=Queue())
prototype.register_object(name='stack',obj=Stack())


class Adapter(object):
    """
    Adapts an object by replacing methods.
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """

    def __init__(self, obj:object, adapted_methods:dict):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)
        self.obj.__dict__.update(adapted_methods)

    def __getattr__(self, attr:str):
        """
        组合优于继承，只有当初始化时候传进来其他对象的实例，就可以用这个方法使用其他类的属性和方法，
        如果不想“继承”，重写就可以
        :param attr:
        :return:
        """
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


# Director
class Director(object):
    """
    指挥者，转换计算流程控制
    """
    def __init__(self):
        """
        calculator:计算者实例
        """
        self.calculator = None

    def calculate_expression(self):
        """
        计算控制流程
        :return:
        """
        self.calculator.new_expression()
        self.calculator.init()
        self.conversion()

    def get_expression(self)->object:
        """
        得到计算后的表达式对象
        :return:
        """
        return self.calculator.expression


# Abstract Builder
class Calculator(object):
    """
    抽象计算者
    """
    def __init__(self):
        """
        expression:表达式对象
        """
        self.expression = None

    def new_expression(self):
        """
        新建表达式对象
        :return:
        """
        self.expression = Expression()


# Concrete Builder
class InfixExpressionCalculate(Calculator):
    """
    中缀表达式的计算，包括中缀变后缀
    """
    def __init__(self,formula:str,formula_type:str):
        """
        中缀表达式初始化
        :param formula:中缀表达式
        :param formula_type: infix:中缀，suffix:后缀，prefix：前缀
        """
        Calculator.__init__(self)
        self.formula = formula
        self.type = formula_type

    def init(self):
        # print(self.expression)
        # exit(0)
        self.expression.formula = self.formula
        self.expression.type = self.type

    def expression_to_suffix(self):
        self.expression.conversion_result = self.infix_to_suffix(formula=self.formula)
    
    @staticmethod
    def infix_to_suffix(formula:str,prototype_queue_stack=prototype)->queue:
        """
        中缀变后缀
        :param formula: 字符表达式
        :param prototype_queue_stack: 堆栈和队列原型

        :return: 结果队列
        """
        _suffix_queue = prototype_queue_stack.clone(name='queue')
        __ops_stack = prototype_queue_stack.clone(name='stack')

        # 运算符优先级,+:并集，-：交集
        ops_right = {'+':1,'-':1}
        for __char in formula:

            # 当元素是操作符时候
            if __char in ops_right.keys():
                while __ops_stack.size() >= 0:
                    # 操作堆栈空的时候直接进栈
                    if __ops_stack.empty():
                        __ops_stack.push(__char)
                        break

                    __ops = __ops_stack.pop()
                    # 当新来的操作符优先级比栈顶元素高的时候进栈
                    if __ops == '[' or ops_right[__char] > ops_right[__ops]:
                        __ops_stack.push(__ops)
                        __ops_stack.push(__char)
                        break
                    else:
                        # 否则操作符出栈并且进表达式栈
                        _suffix_queue.push(__ops)

            # 当元素不是操作符的时候，且是[直接进栈
            elif __char == '[':
                __ops_stack.push(__char)

            # 当元素是]，出栈[]之间的所有操作符
            elif __char == ']':
                while __ops_stack.size():
                    __ops = __ops_stack.pop()
                    if __ops == '[':
                        break
                    else:
                        _suffix_queue.push(__ops)

            # 当元素是运算元素的时候直接入表达式队列
            else:
                _suffix_queue.push(__char)

        # 最后将剩下的操作符放进表达式队列中
        while __ops_stack.size():
            __ops = __ops_stack.pop()
            _suffix_queue.push(__ops)
        
        return _suffix_queue

    def __repr__(self):
        return 'infix formula: %s \n type: %s \n result: %s' % (self.expression.formula,
                                                                self.expression.formula_type,
                                                                self.expression.conversion_result)


class SuffixExpressionCalculate(Calculator):
    def __init__(self,formula:str,formula_type:str):
        """
        后缀表达式初始化
        :param formula:后缀表达式
        :param formula_type: infix:中缀，suffix:后缀，prefix：前缀
        """
        Calculator.__init__(self)
        self.expression.formula = formula
        self.expression.type = formula_type

    def suffix_to_binary_tree(self):
        pass

    def __repr__(self):
        return 'suffix formula: %s \n type: %s \n result: %s' % (self.expression.formula,
                                                                self.expression.formula_type,
                                                                self.expression.conversion_result)


# Product
class Expression(object):
    """
    表达式，用来保存进行转换的式子、类型和结果
    """
    def __init__(self):
        """
        formula:式子，formula_type:式子类型，conversion:转换的结果
        """
        self.formula = None
        self.formula_type = None
        self.conversion_result = None

    def __repr__(self):
        """
        输出
        :return:
        """
        return 'formula: %s | type: %s | result: %s' % (self.formula, self.formula_type, self.conversion_result.data())


# Client
if __name__ == "__main__":
    # 给指挥者配置一个建造者
    director = Director()
    director.calculator = InfixExpressionCalculate(formula='[[F+G]-[[[A-B]+C]+[D-E]]-H]',formula_type='infix')

    # 添加适配器
    adapter = Adapter(obj=director,adapted_methods={"conversion":director.calculator.expression_to_suffix})
    adapter.calculate_expression()
    expression = adapter.get_expression()
    print(expression)

