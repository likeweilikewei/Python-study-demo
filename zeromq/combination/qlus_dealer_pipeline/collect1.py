#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
收集模块
@author: lkw
"""

import zmq

contexts = zmq.Context()

try:
    # 收集模块的pull，接收存储模块的任务，进行收尾工作
    socket_pull = contexts.socket(zmq.PULL)
    socket_pull.connect("tcp://localhost:5562")

except Exception as e:
    print(e)
    socket_pull.close()
    contexts.term()


def collect(pull=socket_pull):
    """
    收集模块，收尾工作
    :param pull: 收集模块的pull
    """
    while True:
        # 接受存储模块的数据任务，进行收尾工作
        context_obj = pull.recv_pyobj()
        context_obj.collect_flag = 1
        print('收集的id:{} ,收尾的信息：{}\n\n'.format(context_obj,'策略处理成功'))

if __name__ == '__main__':
    collect()
