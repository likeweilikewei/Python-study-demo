#! /usr/bin/env python
# -*-coding=utf-8-*-

import json


def eval_json():
    """
    eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    :return:
    """
    kw = {'li':1,'ke':{'wei':1,'s':4}}
    print(eval(json.dumps(kw)))
    # yes
    if kw == eval(json.dumps(kw)):
        print('yes')
    print(json.dumps(kw))
    # str
    print(type(json.dumps(kw)))
eval_json()
