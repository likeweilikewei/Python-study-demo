#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import pandas as pd

r = redis.Redis(host='127.0.0.1', port=6379, db=8, password='123456')

# print(r.hgetall(name='stkRealTimeState:\x01\x01_14901'))
# r.hset(name='stkRealTimeState:{}_14901'.format('000001'), key='pe', value='1')

# redis不支持dataframe，需要将dict转化就可以存入redis,但是存进去是压缩的二进制
# df = pd.DataFrame({'li':['ke', 'wei'],})
# r.hset(name='stkRealTimeState:{}_14901'.format('000001'), key='pe', value=df.to_msgpack(compress='zlib'))
#
# result = r.hget(name='stkRealTimeState:{}_14901'.format('000001'), key='pe')
# print(pd.read_msgpack(result))
# result = float(result)
# print(result)


# # 新建一条键名为"123456"的数据, 包含属性attr_1
# r.hset("123456", "attr_1", 100)
# # 更改键名为"123456"的数据, 更改属性attr_1的值
# r.hset("123456", "attr_1", 200)
#
# # 取出属性attr_1的值
# attr_1 = r.hget("123456", "attr_1")
#
# # 输出看一下(发现属性值已经为str)
# print("-- get attr_1:", attr_1)
#
# # 属性集合
# attr_dict = {
#     "name": "常成功",
#     "alias": "常城",
#     "sex": "male",
#     "height": 175,
#     "postal code": 100086,
#     "Tel": None,
# }
# # 批量添加属性
# r.hmset("123456", attr_dict)
#
# # 取出所有数据(返回值为字典)
# h_data = r.hgetall("123456")
#
# # 输出看一下(取出来的时候都变成了str)
# print("-- get all attr:", h_data)
#
# # 删除属性(可以批量删除)
# r.hdel("123456", "Tel")
#
# # 取出所有属性名
# h_keys = r.hkeys("123456")
#
# print("-- get attr name:", h_keys)

r.lpush('mylist', 23)
r.lpush('mylist', 100)
r.lpush('mylist', 1)
r.lpush('mylist', 30)
r.lpush('mylist', 75)

# hset d-7 field 5
r.hset(name='d-23', key='field', value=555)
r.hset(name='d-100', key='field', value=12)
r.hset(name='d-1', key='field', value=66)
# # dicts = {
# #     30: 10,
# #     75: 33
# # }
# # r.hmset(name='d-', mapping=dicts)
r.hset(name='d-30', key='field', value=6)
r.hset(name='d-75', key='field', value=6)

r.hset(name='d-23', key='age', value=1023)
r.hset(name='d-100', key='age', value=1100)  # redis返回的全是二进制字符串
r.hset(name='d-1', key='age', value=1001)
r.hset(name='d-30', key='age', value=1030)
r.hset(name='d-75', key='age', value=1075)


# 将散列的域（field）用作权重，对mylist进行排序 。
# 具体得说就是将mylist集合里的信息匹配其他集合，并用散列的集合的域进行排序，可以返回其他散列的域
# num是从排序后的列表里进行
result = r.sort(name='mylist', by='d-*->age', get='d-*->field', start=0, num=5,
                desc=False, alpha=False, store=None, groups=False)
print(result)
result2=r.sort('set',alpha=True)
print(result2)
age1 = r.hget(name='d-23', key='age')
print(age1)
