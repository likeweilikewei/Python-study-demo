#!/usr/bin/python
# coding:utf8

"""
Composite

在数据结构中我们了解到可以通过调用某个方法来遍历整个树，当我们找到某个叶子节点后，就可以对叶子节点进行相关的操作。
我们可以将这颗树理解成一个大的容器，容器里面包含很多的成员对象，这些成员对象即可是容器对象也可以是叶子对象。
但是由于容器对象和叶子对象在功能上面的区别，使得我们在使用的过程中必须要区分容器对象和叶子对象，
但是这样就会给客户带来不必要的麻烦，作为客户而已，它始终希望能够一致的对待容器对象和叶子对象。
这就是组合模式的设计动机：组合模式定义了如何将容器对象和叶子对象进行递归组合，使得客户在使用的过程中无须进行区分，
可以对他们进行一致的处理。

组合模式组合多个对象形成树形结构以表示“整体-部分”的结构层次。

组合模式对单个对象(叶子对象)和组合对象(组合对象)具有一致性，它将对象组织到树结构中，可以用来描述整体与部分的关系。
同时它也模糊了简单元素(叶子对象)和复杂元素(容器对象)的概念，使得客户能够像处理简单元素一样来处理复杂元素，
从而使客户程序能够与复杂元素的内部结构解耦。

上面的图展示了计算机的文件系统，文件系统由文件和目录组成，目录下面也可以包含文件或者目录，
计算机的文件系统是用递归结构来进行组织的，对于这样的数据结构是非常适用使用组合模式的。

在使用组合模式中需要注意一点也是组合模式最关键的地方：叶子对象和组合对象实现相同的接口。
这就是组合模式能够将叶子节点和对象节点进行一致处理的原因。
"""


class Component:
    def __init__(self, strName):
        self.m_strName = strName

    def Add(self, com):
        pass

    def Display(self, nDepth):
        pass


class Leaf(Component):
    def Add(self, com):
        print("leaf can't add")

    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print(strtemp)


class Composite(Component):
    def __init__(self, strName):
        Component.__init__(self,strName)
        self.m_strName = strName
        self.c = []

    def Add(self, com):
        self.c.append(com)

    def Display(self, nDepth):
        strtemp = "-" * nDepth
        strtemp = strtemp + self.m_strName
        print(strtemp)
        for com in self.c:
            com.Display(nDepth + 2)


if __name__ == "__main__":
    p = Composite("Wong")
    p.Add(Leaf("Lee"))
    p.Add(Leaf("Zhao"))
    p1 = Composite("Wu")
    p1.Add(Leaf("San"))
    p.Add(p1)
    p.Display(1)
