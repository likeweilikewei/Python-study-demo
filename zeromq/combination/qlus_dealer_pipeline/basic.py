#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
用户数据基本类
@author: lkw
"""

import zmq
import datetime
import pandas as pd


try:
    # 行情接口
    contexts = zmq.Context()
    socket_hq = contexts.socket(zmq.REQ)
    socket_hq.connect("tcp://localhost:5563")
except Exception as e:
    print(e)
    socket_hq.close()
    contexts.term()


class Symbol(object):
    def __init__(self, info, date=datetime.datetime.now()):
        if not isinstance(info, dict) and not isinstance(info,set):
            print('不是dict或者set')
            raise TypeError
        self.__info = info
        self.__code = self.members(self.__info)
        self.__date = date

    def members(self,info):
        """
        选股
        :param info:
        :return:
        """
        if isinstance(info,dict):
            socket_hq.send_pyobj({'indicator':'index','in_type':'plate','op_type':'A','value':[info['index']],'operator':['=']})
            _code = socket_hq.recv_pyobj()
            # _code = set(['000001','000002'])
        elif isinstance(info,set):
            _code = info
        else:
            _code = set([])
        return _code

    @property
    def code(self):
        return self.__code

    def __and__(self, other):
        return Symbol(self.code & other.code)

    def __or__(self, other):
        return Symbol(self.code | other.code)

    """
    左移位代表交集
    """
    def __lshift__(self, other):
        return Symbol(self.code & other.code)

    """
    右移位代表并集
    """
    def __rshift__(self, other):
        return Symbol(self.code | other.code)

    def __str__(self):
        return str(self.code)

    def __repr__(self):
        return str(self.code)


class Order(object):
    """
    进场离场类，存储进场离场的条件
    """
    def __init__(self):
        #财务面
        self.finance = []
        #技术面
        self.technical = []
        #离场条件
        self.leaves = []
        #进场条件
        self.admisss = []
        #分步建仓
        self.steps = []
        #排序条件,区分财务和技术指标排序
        self.stkPkRng = {}
        self.orders = {'valuation':[], 'technical':[]}


class Position(object):
    """
    持仓和交易流水类
    """
    def __init__(self):
        self.stockList = []
        # 当前仓位,卖出和买入都有
        self.percent = 0
        # 当前持仓
        self.positions = pd.DataFrame(
            columns=['no', 'inst', 'name', 'date', 'quatity', 'price', 'count', 'profit', 'last_price',
                     'current_price'])

        # 买卖流水
        self.transactions = pd.DataFrame(
            columns=['status', 'shrId', 'name', 'selectedPrc', 'price', 'quatity', 'tradeMark',
                     'transTm', 'msg', 'profit_loss', 'profit_total', 'buyTm', 'percent', 'last_percent'])
        # 每日资产
        self.totalAssetsList = pd.DataFrame(columns=['asset', 'currentDate', 'total', 'position', 'count'])
        # 当前总资产
        self.totalAssetsLists = 0
        # 手续费
        self.stampDuty = 0
        self.TransferFee = 0
        # 持仓交易后的结果
        self.result = 'position'

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return str(self.result)


class Trade(object):
    """
    买卖判断类，包括条件和结果
    """
    def __init__(self):
        # 买入动作
        self.buy = None
        # 卖出动作
        self.sell = None
        # 买卖判断的结果
        self.result = 'trade'

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return str(self.result)


class Context(object):
    def __init__(self):
        # 进场离场类
        self.order = None
        # 持仓和交易流水类
        self.position = None
        # 选股条件和选股结果类
        self.symbol = None
        # 买卖判断类
        self.trade = None
        # 测试标志
        self.id = 0
        # 存储模块的标志
        self.store_flag = 0
        # 收集模块的标志
        self.collect_flag = 0
        # 行情请求结果
        self.hq = None

    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value
    #     # print(self.__dict__)
    #
    # def __getattr__(self, item):
    #     return self.__dict__.get(item)

    def __str__(self):
        return str(self.__dict__['id'])
        # return self.__dict__

    def __repr__(self):
        return str(self.__dict__['id'])
        # return self.__dict__
