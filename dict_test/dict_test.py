#!/usr/bin/env python
# -*-coding=utf-8-*-




x1 = []
dictx = {}
# print(dictx['ke'])
dictx['type'] = ''.join(x1)
print(dictx)
# print(dictx['li'])  # dict没有key会直接报错，但是用.get就会返回默认值None或者自定义
print(dictx.get('li'))
if 'type' not in dictx.keys():
    print('没有')
else:
    print('有')

if dictx['type']:
    print('有')
else:
    print('没有')

# 键值对互换
# 三种方式交换键值对（前提：值唯一）：
# 1.
mydict={"a":1,"b":2,"c":3}
mydict_new={}
for key,val in mydict.items():
    mydict_new[val]=key
# 2.
mydict={"a":1,"b":2,"c":3}
mydict_new=dict([val,key] for key,val in mydict.items())

# 3.利用zip运算符：
mydict={"a":1,"b":2,"c":3}
mydict_new=dict(zip(mydict.values(),mydict.keys()))
print(mydict_new)


dicts = {'Name': 'Zara', 'Age': 27}

print("Value : %s" %  dicts.get('Age'))
print("Value : %s" %  dicts.get('Sex', "Never"))

# 会出错
# dicts = None
# if '2' in dicts:
#     print('in')

# 字典相加
dict1 = {'usr': 'root', 'pwd': '123456'}
dict2 = {'ip': '127.0.0.1', 'port': '8080', 'usr': 'likewei'}
dict3 = dict(list(dict1.items()) + list(dict2.items()))
print('dict1: ', dict1.items())
print('dict1+dict2:', dict3)
"""
dict1.items()获取字典的键值对的列表
dict1.items() + dict2.items()拼成一个新的列表
dict(dict1.items()+dict2.items())将合并成的列表转变成新的字典
dict2覆盖了dict1
这个方法不优化
"""

"""
python3.5里最好的做法
"""
dict4 = {**dict1, **dict2}
print('dict4:', dict4)

"""
python2和python3.4一下的最好做法
"""
dict5 = dict1.copy()
dict5.update(dict2)
print('dict5:', dict5)

"""
复杂一点的例子
"""
code = ['000001', '000002', '000003']
name = ['平安银行', '万科A', '中海可转债A']
price = ['10', '11', '12']
inc = ['1', '2', '3']
rate = [['1', '1', '1'], ['2', '2', '2'], ['3', '3', '3']]
return_dict_tmp = {'code': code, 'name': name, 'price': price, 'inc': inc}
return_rate_dict_tmp = {'rate{}'.format(i): rate[i] for i in range(3)}
return_dict = {**return_dict_tmp, **return_rate_dict_tmp}
print('return_dict:', return_dict)

# dict是可变对象
dict_test_1 = {}
# print(dict_test_1['li']) 如果没有这个键，会报错
for i in range(3):
    dict_test_1['name'] = i
    print(dict_test_1)
