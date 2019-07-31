#!/usr/bin/env python
# -*-coding=utf-8-*-

from gg import gg_part_to_full, ashare_reflection


def tests():
    keys = list(gg_part_to_full.keys())
    __f = open('./data/gg_part_to_full', 'w', encoding='utf-8')
    for i in range(len(keys)):
        if i % 5 == 0:
            word = "\n'{}': '{}', ".format(keys[i], gg_part_to_full[keys[i]])
        else:
            word = "'{}': '{}', ".format(keys[i], gg_part_to_full[keys[i]])
        __f.write(word)

    values = list(gg_part_to_full.values())
    values = list(set(values))
    print(values)
    print(len(values))
    __f.write('\n\n')
    for j in range(len(values)):
        if j % 5 == 0:
            words = "\n'{}': '{}', ".format(values[j], values[j])
        else:
            words = "'{}': '{}', ".format(values[j], values[j])
        __f.write(words)
    __f.close()
# tests()


def test2():
    keys = list(ashare_reflection.keys())
    __f = open('./data/gg_part_to_full', 'w', encoding='utf-8')
    for i in range(len(keys)):
        if i % 5 == 0:
            word = "\n'{}': '{}', ".format(keys[i], ashare_reflection[keys[i]][:6])
        else:
            word = "'{}': '{}', ".format(keys[i], ashare_reflection[keys[i]][:6])
        __f.write(word)
    __f.close()
test2()
