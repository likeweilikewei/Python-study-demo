#!/usr/bin/env python
# -*-coding=utf-8-*-


import jieba
import jieba.posseg
import jieba.analyse


def test_1():
    """"
    jieba词性标注不能返回中文，不过可以考虑修改jieba函数使之能返回中文词性
    """
    jieba.load_userdict('./jiuniu_corpus/custom_dict_2')
    word = '市盈率在-999999990~-2.677%之间的股票，5日均线连续上涨，like you MaCd顶背离likewei超过\
    周K、个股的指标的值多少周几小霞你好讲个故事讲个笑话你好你是谁你在干什么会唱歌吗现在什么时候现在几点了今天周几今天什么日子\
    天气怎么样布鲁斯.李'
    word_flag = jieba.posseg.cut(word)
    print(word_flag)
    print(type(word_flag))
    for row in word_flag:
        print(row)
        print(type(row))
    for word, flag in word_flag:
        print('word: {}, flag: {}'.format(word, flag))
test_1()
