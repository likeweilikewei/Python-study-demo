#!/usr/bin/env python
# -*-coding=utf-8-*-

from reflection_dict import *


def write_low_index():
    f = open('low_index_list.txt', 'w', encoding='utf-8')
    for i in low_frequency_index.keys():
        print(i)
        f.write('\n' + i)
    f.close()
# write_low_index()


def write_bai_ke():
    f = open('bai_ke.txt', 'w', encoding='utf-8')
    for i in bai_ke:
        print(i)
        f.write('\n' + i)
    f.close()
write_bai_ke()
