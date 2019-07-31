#! /user/bin/env python
# -*- coding=utf-8 -*-


# 随机数，随机读取每一行的数据
import linecache
import random

# print(list(range(0,8,3)))
# print(range(1,8,2))
# print(type(range(8)))

# 随机取
# for i in range(1, 100):  # for循环几次
#     a = random.randrange(0, 500000)  # 1-9中生成随机数
#     # print(a)
#     # 从文件poem.txt中对读取第a行的数据
#     theline = linecache.getline(r'class_four', a)
#     print(theline)

# 读取大型文件的行数
count = 0
fp = open('class_three', "r", encoding='utf-8')
while 1:
    buffer = fp.read(100*1024*1024)
    if not buffer:
        break
    count += buffer.count('\n')
print(count)
print('over')
fp.close()


# 在指定地方插入一行
fp = open('data')
s = fp.read()
fp.close()
a = s.split('\n')
a.insert(4, '5')  # 在第五行插入
s = '\n'.join(a)
fp = open('data', 'w')
fp.write(s)
fp.close()

# 追加
fp = open('data', 'a', encoding='utf-8')
fp.write('\nhello man!')
fp.close()

# 读取
fp = open('data', 'r', encoding='utf-8')
x = fp.read()
print(x)
fp.close()
