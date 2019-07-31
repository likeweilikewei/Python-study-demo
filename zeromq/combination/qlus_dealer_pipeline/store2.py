#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
存储模块
@author: lkw
"""

import zmq

contexts = zmq.Context()

try:
    # 存储模块的pull，接收交易模块的任务
    socket_pull = contexts.socket(zmq.PULL)
    socket_pull.connect("tcp://localhost:5560")

    # 存储模块的push，分发存储模块的任务给收集模块，进行收尾处理
    socket_push = contexts.socket(zmq.PUSH)
    socket_push.connect("tcp://localhost:5561")
except Exception as e:
    print(e)
    socket_pull.close()
    socket_push.close()
    contexts.term()


def store(pull=socket_pull,push=socket_push):
    """
    存储模块，负责将新的持仓和交易流水和指标存储
    :param pull: 存储模块的pull
    :param push: 存储模块的push
    """
    while True:
        # 接受交易模块的数据任务，进行存储
        context_obj = pull.recv_pyobj()
        context_obj.store_flag = 1
        print('存储的id:{} ,存储的信息：{}\n\n'.format(context_obj,context_obj.position.result))

        # 存储后发送给收集模块
        push.send_pyobj(context_obj)

if __name__ == '__main__':
    store()
