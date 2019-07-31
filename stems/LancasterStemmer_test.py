#! /user/bin/env python
# -*- coding=utf-8 -*-

from nltk.stem.lancaster import LancasterStemmer


def stems(all_texts_tokenized):
    """
    词干化,针对英语,会自动将英语转化为小写
    :param all_texts_tokenized:分词后的语料，格式：格式：[['词语','词语','词语'],['词语','词语','词语']...]
    :return:词干化的语料
    """
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in docment] for docment in all_texts_tokenized]
    return texts_stemmed

result = stems([['工商银行', '的', '现价', '是', '多少', 'eatting']])
print(result)
