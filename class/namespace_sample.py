#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_1():
    """
    只要inputs不改变，它身上的标签就不会改变，反之标签都会改变
    :return:
    """
    class A:
        def __init__(self, inputs):
            self.name = inputs

        def funca(self):
            inputs_tmp = self.name.lower()
            print("tmp : %s" % inputs_tmp)

    a = A('Like You.')
    print(a.name)
    a.funca()
    print(a.name)
# test_1()


def test_2():
    class B:
        def __init__(self, input1):
            self.name1 = input1
            self.name2 = None

        def funcb(self):
            self.name2 = self.name1.lower()
            print("name1: %s\nname2: %s" % (self.name1, self.name2))

    b = B('Like You.')
    print('name1: {}\nname2: {}'.format(b.name1, b.name2))
    b.funcb()
test_2()
