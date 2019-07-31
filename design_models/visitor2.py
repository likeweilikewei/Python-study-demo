# encoding=utf-8
#
# by panda
# 访问模式

"""
访问者模式：表示一个作用于某对象结构中的各元素的操作。它可以使你在不改变各元素的类的前提下定义作用于这些元素的新操作。
访问者模式适用于数据结构相对稳定而基于该数据结构的操作需要经常扩展的系统。因为该模式的优点就是增加新的操作很容易。
"""


def printInfo(info):
    print(info)


# 基本数据结构：
class Person():
    def Accept(self, visitor):
        pass


class Man(Person):
    type = '男人'

    def Accept(self, visitor):
        visitor.GetManConclusion(self)


class Woman(Person):
    type = '女人'

    def Accept(self, visitor):
        visitor.GetWomanConclusion(self)


# 基于数据结构的操作
class Action():
    def GetManConclusion(self, person):
        pass

    def GetWomanConclusion(self, person):
        pass


class Success(Action):
    type = '成功'

    def GetManConclusion(self, person):
        printInfo('%s %s时，背后多半有一个伟大的女人' % (person.type, self.type))

    def GetWomanConclusion(self, person):
        printInfo('%s %s时，背后大多有一个不成功的男人' % (person.type, self.type))


class Failing(Action):
    type = '失败'

    def GetManConclusion(self, person):
        printInfo('%s %s时，闷头喝酒，谁也不用劝' % (person.type, self.type))

    def GetWomanConclusion(self, person):
        printInfo('%s %s时，眼泪汪汪，谁也劝不了' % (person.type, self.type))


class Love(Action):
    type = '恋爱'

    def GetManConclusion(self, person):
        printInfo('%s %s时，凡是不懂也要装懂' % (person.type, self.type))

    def GetWomanConclusion(self, person):
        printInfo('%s %s时，遇事懂也装作不懂' % (person.type, self.type))


# 对象结构类：遍历数据结构的操作
class ObjectStructure:
    elements = []

    def Attach(self, element):
        self.elements.append(element)

    def Detach(self, element):
        self.elements.remove(element)

    def Display(self, visitor):
        for e in self.elements:
            e.Accept(visitor)


def clientUI():
    o = ObjectStructure()
    o.Attach(Man())
    o.Attach(Woman())

    o.Display(Success())
    o.Display(Failing())
    o.Display(Love())
    return


if __name__ == '__main__':
    clientUI()
