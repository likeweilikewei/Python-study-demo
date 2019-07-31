# encoding=utf-8
#
# by panda
# 中介者模式
"""
中介者模式：用一个中介对象来封装一系列的对象交互。中介者使各对象不需要显式地相互引用，从而使其耦合松散，
而且可以独立地改变它们之间的交互。
一般应用于一组对象以定义良好但是复杂的方式进行通信的场合。
优点：降低了各个模块的耦合性。
缺点：中介对象容易变得复杂和庞大。
"""


def printInfo(info):
    print(info)


# 抽象中介者
class Mediator():
    def Send(self, message, colleague):
        pass


# 抽象同事类
class Colleague():
    mediator = None

    def __init__(self, mediator):
        self.mediator = mediator


# 具体同事类
class ConcreteColleague(Colleague):
    name = ''

    def __init__(self, name, mediator):
        self.name = name
        Colleague.__init__(self, mediator)

    def Send(self, message):
        self.mediator.Send(message, self)

    def Notify(self, message):
        printInfo('%s得到对方消息：%s' % (self.name, message))


# 具体中介者
class ConcreteMediator(Mediator):
    name = ''
    colleague1 = None
    colleague2 = None

    def __init__(self, name):
        self.name = name

    def Send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.Notify(message)
        else:
            self.colleague1.Notify(message)


def clientUI():
    mediator = ConcreteMediator('联合国')
    USA = ConcreteColleague('美国', mediator)
    mediator.colleague1 = USA
    Iraq = ConcreteColleague('伊拉克', mediator)
    mediator.colleague2 = Iraq

    USA.Send('不准研制核武器，否则要发动战争')
    Iraq.Send('我们没有核武器，也不怕侵略')
    return


if __name__ == '__main__':
    clientUI()
