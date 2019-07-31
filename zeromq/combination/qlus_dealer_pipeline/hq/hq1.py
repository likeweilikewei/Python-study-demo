#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
hq接口模块
@author: lkw
"""

import zmq

try:
    contexts = zmq.Context()
    # hq接口模块
    sockets = contexts.socket(zmq.REP)
    sockets.connect("tcp://localhost:5564")
    # 板块接口
    socket_plate = contexts.socket(zmq.REQ)
    socket_plate.connect("tcp://localhost:5565")
    # 财务接口
    socket_finance = contexts.socket(zmq.REQ)
    socket_finance.connect("tcp://localhost:5566")
    # 技术接口
    socket_technical = contexts.socket(zmq.REQ)
    socket_technical.connect("tcp://localhost:5565")
    # 基本面接口
    socket_fundamentals = contexts.socket(zmq.REQ)
    socket_fundamentals.connect("tcp://localhost:5565")
    # 持仓和交易流水接口
    socket_pos_trans = contexts.socket(zmq.REQ)
    socket_pos_trans.connect("tcp://localhost:5565")
except Exception as e:
    print(e)
    socket_plate.close()
    sockets.close()
    socket_finance.close()
    socket_technical.close()
    socket_fundamentals.close()
    socket_pos_trans.close()
    contexts.term()


def hq():
    """
    hq接口模块，提供行情和持仓交易流水
    """
    while True:
        # 接受各个模块的行情请求和持仓和交易流水请求
        context_obj = sockets.recv_pyobj()
        print('接口收到的行情：{}\n\n'.format(context_obj))
        if not isinstance(context_obj,dict):
            sockets.send_pyobj({'query':context_obj,'result':None,'result_type':'error','message':'行情请求格式不对。'})
            continue
        else:
            # print('context:{}'.format(context_obj))
            __type = context_obj.get('in_type',None)
            # 请求板块相关数据
            if __type == 'plate':
                # 请求板块
                __data = {'indicator':context_obj.get('indicator'),'value':context_obj.get('value')[0]}
                socket_plate.send_pyobj(__data)
                __result_plate = socket_plate.recv_pyobj()

                # 返回消息
                sockets.send_pyobj({'query':context_obj,'result':__result_plate,'result_type':'set','message':'板块请求成功。'})
                print('行情的信息：{}\n\n'.format({'query': context_obj, 'result': __result_plate, 'result_type': 'set', 'message': '板块请求成功。'}))
            # 请求技术面相关数据
            elif __type == 'technical':
                pass
            # 请求财务相关数据
            elif __type == 'finance':
                pass
            # 请求基本面相关数据
            elif __type == 'fundamentals':
                pass
            # 请求持仓相关数据
            elif __type == 'positions':
                pass
            # 请求交易流水相关数据
            elif __type == 'transactions':
                pass
            # 请求异常
            else:
                sockets.send_pyobj({'query': context_obj, 'result': None, 'result_type': 'error', 'message': '行情请求没有指标类型。'})
                continue

if __name__ == '__main__':
    hq()
