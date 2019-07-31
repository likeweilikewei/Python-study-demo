#! /user/bin/env python
# -*- coding=utf-8 -*-


ls = [1, 2, 3]
print(','.join(str(s) for s in ls if s not in [None]))  # .join接受一个序列或者生成器
print(str(s) for s in ls if s not in [None])  # 这是一个生成器
