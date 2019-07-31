#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
策略解析、选股、买卖判断
@author: lkw
"""

import zmq
import time

from basic import *

try:
    # 流程接口
    contexts = zmq.Context()
    socket = contexts.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5555")
    # 行情接口
    socket_hq = contexts.socket(zmq.REQ)
    socket_hq.connect("tcp://localhost:5563")
except Exception as e:
    print(e)
    socket.close()
    socket_hq.close()
    contexts.term()


def distribute_query(query:object,sockets=socket):
    """
    分发请求，模式是dealer、router
    :param query: 请求
    :param sockets: zmq接口
    :return:结果对象
    """
    if not isinstance(query,object):
        raise Exception('distribute is not object.')
    # print(query,'------------------')
    # print(query)
    sockets.send_pyobj(obj=query)
    # query_result = sockets.recv_pyobj()
    # print('query result:{}'.format(query_result))
    # return query_result


if __name__ == '__main__':
    id_tmp = 0
    while True:
        # 测试id
        id_tmp += 1
        # 选股条件和选股后的结果
        symbol = Symbol(info={'id':id_tmp,'index':'000001.SH'})
        # 进场离场类
        order = Order()
        # 持仓和交易流水类
        position = Position()
        # 交易类
        trade = Trade()
        # 总的信息类
        context = Context()
        context.order = order
        context.symbol = symbol
        context.position = position
        context.trade = trade
        context.id = id_tmp
        # print(context)
        # print(Context.__dict__)
        print('选股结果为：{}'.format(context.symbol))
        print('开始分发解析选股后的任务，id:{}'.format(context))
        distribute_query(query=context)
        time.sleep(1)
