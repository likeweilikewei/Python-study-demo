#! /usr/bin/env python
# -*- coding=utf-8 -*-

txt = open('index', 'r', encoding='utf-8')
txt_dict = open('index_dict', 'w', encoding='utf-8')
count = 0
len_count = 0
"""每三条转一行"""
# try:
#     for line in txt:
#         # print('line: {}'.format(line))
#         # print('line type: {}'.format(type(line)))
#         line = line.strip('\n')
#         line = line.strip(' ')
#         line_list = line.split(' ')
#         # print(line_list)
#         # print('line split: {}'.format(line.split(' ')))
#         if line_list[-1] == '' or line_list[0] == '':
#             print('yes')
#             continue
#         count += 1
#         if count % 3 == 0:
#             line_str = "'{}': '{}', \n".format(line_list[-1], line_list[0])
#         else:
#             line_str = "'{}': '{}', ".format(line_list[-1], line_list[0])
#         txt_dict.write(line_str)
# finally:
#     txt.close()
#     txt_dict.close()

"""每120个字符长度转一行"""
try:
    for line in txt:
        # print('line: {}'.format(line))
        # print('line type: {}'.format(type(line)))
        lines = line.strip('\n')
        lines = lines.strip(' ')
        line_list = lines.split(' ')
        # print(line_list)
        # print('line split: {}'.format(line.split(' ')))
        if line_list[-1] == '' or line_list[0] == '':
            continue
        line_str = "'{}': '{}', ".format(line_list[-1], line_list[0])
        len_count += len(line_str)
        count += 1
        if len_count >= 120:
            line_str_result = '\n' + line_str
            print('len: {}'.format(len_count - len(line_str)))
            len_count = len(line_str)
            print('count: {}'.format(count - 1))
            count = 0
        else:
            print(count)
            line_str_result = line_str
        txt_dict.write(line_str_result)
finally:
    txt.close()
    txt_dict.close()
