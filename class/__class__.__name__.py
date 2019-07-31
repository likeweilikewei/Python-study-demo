#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
谁去调用__class__.__name__就是哪个类名
Test_2
"""


class Test_1:
    def test_1(self):
        print(self.__class__.__name__)


class Test_2(Test_1):
    def test_2(self):
        self.test_1()

test = Test_2()
test.test_2()
