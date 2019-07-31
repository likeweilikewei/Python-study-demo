#!/usr/bin/env python
# -*-coding=utf-8-*-


import jieba
import jieba.posseg
import jieba.analyse


def test_1():
    """"
    基本方法：jieba.analyse.extract_tags(sentence, topK)
    需要先import jieba.analyse，其中sentence为待提取的文本，topK为返回几个TF/IDF权重最大的关键词，默认值为20。
    关键词提取
    频率相同的话就按照数字、字母、文字排序。
    还会自动去掉停用词、标点符号。打乱了文本原有的顺序。
    lcut可以提取百分号，而possea则不能，两者都不能去停用词
    ['均线', '999999990', '2.677%', 'like', 'MaCd', 'likewei', 'MACD', '顶背离', '市盈率', '连续']
    lcut: ['市盈率', '在', '999999990', '~', '-', '2.677%', '之间', '的', '股票', '，', '5', '日', '均线',
    '连续', '上涨', '，', 'like', ' ', 'you', ' ', 'MaCd', '顶背离', 'likewei', ' ', 'MACD', '，', '均线', '是']

    posseg: ['市盈率', '在', '999999990', '~', '-', '2.677', '%', '之间', '的', '股票', '，', '5', '日',
    '均线', '连续', '上涨', '，', 'like', ' ', 'you', ' ', 'MaCd', '顶背离', 'likewei', ' ', 'MACD', '，',
    '均线', '是']
    """
    jieba.analyse.set_stop_words('./jiuniu_corpus/stop_words')
    jieba.load_userdict('./jiuniu_corpus/custom_dict_2')
    word = '市盈率在-999999990~-2.677%之间里的股票，5日均线连续上涨，二百四十日均线大于，like you MaCd顶背离likewei MACD，均线是5日五日'
    word_flag = jieba.analyse.extract_tags(word)
    result1 = jieba.lcut(word)
    result2 = jieba.posseg.cut(word)
    print(word_flag)
    print('lcut: {}'.format(result1))
    list1 = []
    print('posseg cut:{}'.format(result2))
    for words, flag in result2:
        list1.append(words)
    print('posseg: {}'.format(list1))
test_1()
