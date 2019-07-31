#! /user/bin/env python
# -*- coding=utf-8 -*-


# ls = [1, 2, 3]
# print(','.join(str(s) for s in ls if s not in [None]))  # .join接受一个序列或者生成器
# print(str(s) for s in ls if s not in [None])  # 这是一个生成器

types = '1,2'
type_list = types.split(',')
print(type_list)

# AttributeError: 'NoneType' object has no attribute 'split'
# block = None
# block_list = block.split(',')
# print(block_list)
