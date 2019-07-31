#! /user/bin/env python
# -*- coding=utf-8 -*-

"""None 不可以进行str的转化，只有byte可以str"""
result = str(b'None', encoding='utf-8')
print(result)
