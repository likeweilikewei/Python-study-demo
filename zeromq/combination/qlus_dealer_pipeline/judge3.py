#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
买卖判断
@author: lkw
"""

import zmq

contexts = zmq.Context()

try:
    # 买卖判断的pull
    socket_pull = contexts.socket(zmq.PULL)
    socket_pull.connect("tcp://localhost:5556")
    # 买卖判断的push
    socket_push = contexts.socket(zmq.PUSH)
    socket_push.connect("tcp://localhost:5557")
except Exception as e:
    print(e)
    socket_pull.close()
    socket_push.close()
    contexts.term()


def trade_judge(pull=socket_pull, push=socket_push):
    """
    买卖判断
    :param pull: 买卖判断的pull
    :param push: 买卖判断的push
    """
    while True:
        # 接受用户数据,解析选股
        context_obj = pull.recv_pyobj()
        context_obj.trade.result = {'buy': {'stock': '000001.SH', 'price': 6.38, 'quantity': 200}}
        print('买卖判断的id:{} ,买卖判断的结果：{}'.format(context_obj, context_obj.trade))

        # 解析选股后分发给买卖判断模块
        push.send_pyobj(context_obj)


if __name__ == '__main__':
    trade_judge()
