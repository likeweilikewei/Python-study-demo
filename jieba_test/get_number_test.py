#!/usr/bin/env python
# -*-coding=utf-8-*-


import jieba
import jieba.analyse

jieba.load_userdict('./jiuniu_corpus/custom_dict')

word = '市盈率在999999990~-2.677%之间的股票'
# word = '国家队有哪些股票'

# word = '601398.SZ的现价'
# jieba.analyse.set_stop_words('./jiuniu_corpus/stop_words')
# cut_word = jieba.analyse.extract_tags(word, 10)
cut_word = jieba.lcut(word)
print(cut_word)
print(len('601398'))


# print(cut_word)
#
# for str in cut_word:
#     print(type(str))
#     print(str)
#     print(str.isdigit())
#
# str = "1.11"  # Only digit in this string
# print(str.isdigit())  # 只能针对整数
#
# str = "this is string example....wow!!!"
# print(str.isdigit())

# number_list = []
# negative_number_flag = False
# negative_number_next = False
# for word in cut_word:
#     # print(type(word))
#     # if isinstance(word, str):
#         # print(type(word))
#         # print('right')
#     if '%' in word:
#         words = word.strip('%')
#         words = float(words) / 100
#         if negative_number_flag and negative_number_next:
#             negative_number_next = False
#             negative_number_flag = False
#             number_list.append(-words)
#         else:
#             number_list.append(words)
#     try:
#         if negative_number_flag and negative_number_next:
#             number = float(word)
#             number_list.append(-number)
#             # print('number:', number)
#             negative_number_next = False
#             negative_number_flag = False
#         else:
#             number = float(word)
#             number_list.append(number)
#     except Exception as e:
#         if word in ['-', '-']:
#             negative_number_flag = True
#             negative_number_next = True
#             print('检测到了')
# print(number_list)
# number_list.sort()
# print(number_list)


# def get_number_from_str_list(words):
#     """
#     从分词后语句中提取数值
#     :param words: 分词后的语句
#     :return: 数值列表
#     """
#     number_list = []
#     negative_number_flag = False
#     negative_number_next = False
#     for word in words:
#         if '%' in word:
#             words = word.strip('%')
#             words = float(words) / 100
#             if negative_number_flag and negative_number_next:
#                 negative_number_next = False
#                 negative_number_flag = False
#                 number_list.append(-words)
#             else:
#                 number_list.append(words)
#         try:
#             if negative_number_flag and negative_number_next:
#                 number = float(word)
#                 number_list.append(-number)
#                 negative_number_next = False
#                 negative_number_flag = False
#             else:
#                 number = float(word)
#                 number_list.append(number)
#         except Exception as e:
#             if word in ['-', '-']:
#                 negative_number_flag = True
#                 negative_number_next = True
#     number_list.sort()
#     return number_list
#
# r = get_number_from_str_list(cut_word)
# print(r)

# jieba返回指定词性
# jieba.load_userdict('./jiuniu_corpus/custom_dict')
# sentence = '000001.sz的现价'
# # result = jieba.analyse.extract_tags(sentence, 10, allowPOS=('gg'))
# # print(result)
#
# results = jieba.analyse.textrank(sentence, topK=1, withWeight=False, allowPOS=('gg', 'zb'))
# print(results)
#
# # 返回词性列表
# import jieba.posseg as pseg
# words = pseg.cut(sentence=sentence)
# for word, flag in words:
#     # print('%s, %s' % (word, flag))
#     if flag == 'gg':
#         print('%s, %s' % (word, flag))
