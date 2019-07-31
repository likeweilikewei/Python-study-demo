#!/usr/bin/env python
# -*-coding=utf-8-*-


from reflection_dict import *

plate_list = industry_list + conseption_list + region_list + index_list

# end_word = ['是多少？', '']
# f = open('./corpus/stock_indicators', 'w+', encoding='utf-8')
# for i in range(len(ashare_list)):
#     for j in range(len(indication_list_all)):
#         for k in range(len(end_word)):
#             word = ashare_list[i]+'的'+indication_list_all[j]+end_word[k]+'\n'
#             word2 = ashare_list[i]+indication_list_all[j]+end_word[k]+'\n'
#             f.write(word)
#             f.write(word2)
# f.close()

# front_word = ['板块里', '里', '概念里']
# middle_word = ['区间在0到0', '不低于0', '不高于0', '不高过0', '不低过0', '低于0', '高于0', '超过0', '不超过0', '大于0', '不大于0',
#             '少于0', '不少于0', '小于0', '不小于0', '多于0', '不多于0', '0到0之间', '排名', '排行', '最高', '最低', '比较高',
#             '比较低', '较高', '较低', '很低', '很高', '异常高', '异常低', '非常高', '非常低', '特别高', '特别低', '小于等于0',
#             '大于等于0', '降序', '升序', '范围在0到0', '取值在0到0', '从低到高', '从小到大', '从高到低', '从大到小', '低出0',
#             '高出0', '没超过0', '没低于0', '没多于0', '没高于0', '没低过0', '没少于0', '没小于0', '没大于0', '没低过', '没高过',
#             '不超出0', '在0到0间', '在0~-0', '大于0小于0', '小于0大于0']
# end_word = ['的股票', '的股票有哪些', '的有哪些', '的有哪些股票', '的']
# f = open('./corpus/plate_indicators', 'w+', encoding='utf-8')
# print(len(plate_list))
# for i in range(len(plate_list)):
#     for j in range(len(indication_list)):
#         for m in range(len(front_word)):
#                 for k in range(len(middle_word)):
#                         for h in range(len(end_word)):
#                                 word = plate_list[i]+front_word[m]+indication_list[j]+middle_word[k]+end_word[h]+'\n'
#                                 # word2 = indication_list[j]+middle_word[k]+'的'+plate_list[i]+end_word[h]+'\n'
#                                 # word = plate_list[i]+'\n'
#                                 # print(word)
#                                 f.write(word)
#                                 # f.write(word2)
# f.close()

# end_word = ['行情', '的行情', '的走势', '的K线', 'k线', '分时', '日K', '周K', '月K', '日度',
#             '的k线', '的日k', '的周k', '的月k', '分钟线', '的公告', '的研报', '的资讯', '的新闻',
#             '的情况', '的财报', '简况']
# f = open('./corpus/stock_market', 'w+', encoding='utf-8')
# for i in range(len(ashare_list)):
#     for j in range(len(end_word)):
#         word = ashare_list[i]+end_word[j]+'\n'
#         f.write(word)
# f.close()

# front_word = ['分析']
# end_word = ['的建议', '的投顾建议', '好不好', '怎么样', '值得入手吗', '值得投资吗']
# f = open('./corpus/stock_advice', 'w+', encoding='utf-8')
# for i in range(len(ashare_list)):
#     for j in range(len(end_word)):
#         word = ashare_list[i]+end_word[j]+'\n'
#         word2 = '分析'+ashare_list[i] + '\n'
#         f.write(word)
#         f.write(word2)
# f.close()

# end_word = ['的股票', '的股票有哪些', '的有哪些', '的有哪些股票', '的', '']
# front_word = ['板块', '', '概念', '行业']
# technical_words = ['5日均线连续5天上涨', '股价回踩10日均线', '股价回踩20日均线', '股价上探5日均线', '股价上探10日均线',
#                    '多头排列', '10日均线连续10日上涨', '5日均线上穿10日均线', '5日均线上穿20日均线', 'kdj金叉', 'kdj死叉',
#                    'kdj低位死叉', 'kdj低位金叉', 'kdj高位金叉', 'kdj高位死叉', '上穿boll上轨', '上穿boll中轨', '下穿boll中轨',
#                    '下穿boll下轨', 'boll线开口变大', 'boll线开口变小', 'macd指标金叉', 'macd指标死叉', 'macd指标零轴以上金叉',
#                    'macd指标零轴以上死叉', 'macd指标零轴以下金叉', 'macd指标零轴以下死叉', 'macd顶背离', 'macd底背离',
#                    '成交量缩量', '成交量温和放量', '成交量明显放量', '成交量巨量放量', '成交量天量放量']
# f = open('./corpus/plate_technical', 'w+', encoding='utf-8')
# for i in range(len(plate_list)):
#     for h in range(len(front_word)):
#         for j in range(len(technical_words)):
#             for k in range(len(end_word)):
#                 word = plate_list[i]+front_word[h]+technical_words[j]+end_word[k]+'\n'
#                 f.write(word)
# f.close()

# middle_word = ['区间在0到0', '不低于0', '不高于0', '不高过0', '不低过0', '低于0', '高于0', '超过0', '不超过0', '大于0', '不大于0',
#             '少于0', '不少于0', '小于0', '不小于0', '多于0', '不多于0', '0到0之间', '排名', '排行', '最高', '最低', '比较高',
#             '比较低', '较高', '较低', '很低', '很高', '异常高', '异常低', '非常高', '非常低', '特别高', '特别低', '小于等于0',
#             '大于等于0', '降序', '升序', '范围在0到0', '取值在0到0', '从低到高', '从小到大', '从高到低', '从大到小', '低出0',
#             '高出0', '没超过0', '没低于0', '没多于0', '没高于0', '没低过0', '没少于0', '没小于0', '没大于0', '没低过', '没高过',
#             '不超出0', '在0到0间', '在0~0', '大于0小于0', '小于0大于0']
# end_word = ['的股票', '的股票有哪些', '的有哪些', '的有哪些股票', '的']
# f = open('./corpus/indicators_select', 'w+', encoding='utf-8')
# for j in range(len(indication_list)):
#     for h in range(len(middle_word)):
#         for k in range(len(end_word)):
#                 word = indication_list[j]+middle_word[h]+end_word[k]+'\n'
#                 f.write(word)
# f.close()

# f = open('./corpus/indicators_teach', 'w+', encoding='utf-8')
# for j in range(len(indication_list)):
#         word = indication_list[j]+'\n'
#         word2 = indication_list[j] + '的解释\n'
#         word3 = indication_list[j] + '是什么意思\n'
#         word4 = indication_list[j] + '的百科\n'
#         f.write(word)
#         f.write(word2)
#         f.write(word3)
#         f.write(word4)
# f.close()

# front_word = ['板块', '', '概念', '行业']
# end_word = ['的股票', '的股票有哪些', '有哪些', '有哪些股票', '']
# f = open('./corpus/plate_select', 'w+', encoding='utf-8')
# for j in range(len(plate_list)):
#     for h in range(len(front_word)):
#         for k in range(len(end_word)):
#                 word = plate_list[j]+front_word[h]+end_word[k]+'\n'
#                 f.write(word)
# f.close()

# end_word = ['的股票', '的股票有哪些', '有哪些', '有哪些股票', '']
# f = open('./corpus/technical_select', 'w+', encoding='utf-8')
# for i in range(len(technical_list)):
#     for j in range(len(end_word)):
#         word = technical_list[i]+end_word[j]+'\n'
#         f.write(word)
# f.close()

# 生成股票代码的词性
# f = open('./corpus/custom_dict', 'a', encoding='utf-8')
# for name, stock in ashare_reflection.items():
#     stocks = stock[:6]
#     f.write('\n' + str(stocks) + ' ' + 'gg')
# f.close()

# 生成股票简称的词性
# f = open('./corpus/custom_dict', 'w', encoding='utf-8')
# for part in stock_part_list:
#     f.write('\n' + str(part) + ' ' + 'gg')
# f.close()

# 生成指标简称的词性
f = open('./corpus/custom_dict', 'a', encoding='utf-8')
for index in index_to_standard.keys():
    f.write('\n' + str(index) + ' ' + 'zb')
f.close()
