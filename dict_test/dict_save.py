#!/usr/bin/env python
# -*-coding=utf-8-*-

from reflection_dict import ashare_reflection

part_to_name = {}
# part_to_name = dict(zip(ashare_reflection.values(), ashare_reflection.keys()))
# print(part_to_name)

part_to_name2 = dict([['a',1]])
# print(part_to_name2)

part_to_name = dict([value[:6], key] for key, value in ashare_reflection.items())
print(part_to_name)
f = open('part_to_name', 'a', encoding='utf-8')
f.write('{}'.format(part_to_name))
f.close()
