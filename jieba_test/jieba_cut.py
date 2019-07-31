#!/usr/bin/env python
# -*-coding=utf-8-*-


import jieba
import jieba.posseg
import jieba.analyse


def test_1():
    """"
    jieba词性标注不能返回中文，不过可以考虑修改jieba函数使之能返回中文词性
    有符号的自定义词不能成功
    jieba会尽量长的匹配，除非词频大于等于5倍
    jieba没有办法定义单个字
    可以自定义带.的单词
    不识别不低于
    """
    jieba.load_userdict('./jiuniu_corpus/custom_dict_2')
    word = '市盈率在999999990~-2.677%之间的股票，5日均线连续上涨，\
    like you MaCd顶背离likewei MACD 000001, 铁路、船舶、航空航天和其他运输设备制造业\
    中小板指数粤PM2.5 PM2-5资产总计除以资产总额低于-3W&R 标准・普尔500指数 QFⅡPre-IPO Van Eck GlobalADTM高于0.\
    5中国平安保险(集团)股份有限公司“孤儿”保单服务不低于0较低最低ADTM高过0.5工业4.0布鲁斯.李猪'
    word_flag = jieba.posseg.cut(word)
    print(word_flag)
    for word, flag in word_flag:
        print('word: {}, flag: {}'.format(word, flag))
test_1()

# []为空
if []:
    print('yes')
else:
    print('no')
