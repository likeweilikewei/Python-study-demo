#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
交易模块
@author: lkw
"""

import zmq
import pandas as pd

contexts = zmq.Context()

try:
    # 交易模块的pull
    socket_pull = contexts.socket(zmq.PULL)
    socket_pull.connect("tcp://localhost:5558")
    # 交易模块的push
    socket_push = contexts.socket(zmq.PUSH)
    socket_push.connect("tcp://localhost:5559")
except Exception as e:
    print(e)
    socket_pull.close()
    socket_push.close()
    contexts.term()


def trade(pull=socket_pull,push=socket_push):
    """
    交易模块，负责更新持仓和交易流水
    :param pull: 交易模块的pull
    :param push: 交易模块的push
    """
    while True:
        # 接受买卖判断数据,进行交易,更新持仓和交易流水
        context_obj = pull.recv_pyobj()
        context_obj.position.result = {'positions':pd.DataFrame(context_obj.trade.result['buy'],index=[0]),
                                       'transactions':pd.DataFrame(context_obj.trade.result['buy'],index=[0])}
        print('交易的id:{} ,交易的结果：{}\n\n'.format(context_obj,context_obj.position.result))

        # 交易后发送给存储模块
        push.send_pyobj(context_obj)

if __name__ == '__main__':
    trade()
