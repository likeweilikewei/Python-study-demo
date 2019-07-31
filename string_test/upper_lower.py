#! /user/bin/env python
# -*- coding=utf-8 -*-


def test_1():
    """
    把所有字符中的小写字母转换成大写字母
    :return:HELLO WORLD!
    """
    strs = "hELLO world!"
    print(strs.upper())


def test_2():
    """
    把所有字符中的大写字母转换成小写字母
    :return:hello world!
    """
    str1 = "hELLO world! 李可威"
    print(str1.lower())


def test_3():
    """
    把第一个字母转化为大写字母，其余小写
    :return:Hello world!
    """
    str2 = "hELLO world!"
    print(str2.capitalize())


def test_4():
    """
    把每个单词的第一个字母转化为大写，其余小写
    :return:Hello World!
    """
    str3 = "hELLO world!"
    print(str3.title())
test_1()
test_2()
test_3()
test_4()
