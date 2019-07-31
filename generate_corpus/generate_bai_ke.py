#!/usr/bin/env python
# -*-coding=utf-8-*-

from robot_dict import bai_ke


def tests():
    keys = bai_ke
    __f = open('./data/bai_ke', 'w', encoding='utf-8')
    for i in range(len(keys)):
        if i % 5 == 0:
            word = "\n'{}', ".format(keys[i])
        else:
            word = "'{}', ".format(keys[i])
        __f.write(word)
tests()
