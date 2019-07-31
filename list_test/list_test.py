#! /user/bin/env python
# -*- coding=utf-8 -*-

lists = ['pe', 'ps', 'amount']
old_lists = ["stkRealTimeState:*->shrCd", "stkRealTimeState:*->shrNm", "stkRealTimeState:*->nMatch",
             "stkRealTimeState:*->riseAndFallRate"]
# 如果list为空，直接报IndexError: list index out of range
# listss = []
# old_lists.extend(["stkRealTimeState:*->" + listss[i]
#                                                                        for i in range(len(lists))])
# print(old_lists)
# print(["stkRealTimeState:*->" + lists[i]
#                                                                        for i in range(len(lists))])

for i in range(1):
    print('input')
    print(i)

if 0:
    print('0 is true')

for i in ['li', 'ke', 'wei']:
    print(i)

# 将其中的str转化为float,只能针对单个列表的情况
# __range_value_tmp = [['1', '2'], ['3'], ['4']]
__range_value_tmp = ['1', '3', '5']
range_value_list = list(map(float, __range_value_tmp))
print('range_value_list:', range_value_list)

if False == None:
    print('False is None')
else:
    print('False is not None')

if None == None:
    print('None is None')

if not False:
    print('False is 0')
else:
    print('False is not 0')

if not None:
    print('None is 0')
else:
    print('None is not 0')


def type_test():
    a = [1,2,3]
    if isinstance(a,list):
        print('yes')
    else:
        print('no')
    if not isinstance(a, list):
        print('no')
    else:
        print('yes')
# type_test()

x = ['1','2']
y = ['4','5']
x = x+y
print(x)
print(x+y)


