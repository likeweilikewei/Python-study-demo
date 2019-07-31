#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
sorted碰到nan会重新开始排序
"""

import numpy as np

lists = ['pe', 'ps', 'amount']
old_lists = [1,4,np.nan,3,-1,2]
s = sorted(old_lists,reverse=True)
print(s)
