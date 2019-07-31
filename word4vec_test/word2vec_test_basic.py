#!/usr/bin/env python
# -*-coding=utf-8-*-


from gensim.models import word2vec

# 引入日志配置
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 引入数据集
raw_sentences = ["the quick brown fox jumps over the lazy dogs", "yoyoyo you go home now to sleep"]

# 切分词汇
sentences= [s.split() for s in raw_sentences]
print(sentences)

# 构建模型
model = word2vec.Word2Vec(sentences, min_count=1)
model.save('text8.model')
model1 = word2vec.Word2Vec.load('text8.model')
s='you  home'
print(s.split())
ss = model.most_similar(s.split())
print('ss:', ss)

# 进行相关性比较
result = model.similarity('dogs', 'you')
print(result)
