#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
交易到存储的代理
@author: lkw
"""

import zmq


def main():
    try:
        context = zmq.Context(1)
        # 接受交易模块的pull任务
        frontend = context.socket(zmq.PULL)
        frontend.bind("tcp://*:5559")

        # 将交易模块的任务分发给存储模块进行存储
        backend = context.socket(zmq.PUSH)
        backend.bind("tcp://*:5560")

        # zmq.device()里有个while True
        zmq.device(zmq.STREAMER, frontend, backend)
    except Exception as e:
        print(e)
        print("bringing down zmq device")
    finally:
        # pass
        frontend.close()
        backend.close()
        context.term()


if __name__ == "__main__":
    main()
