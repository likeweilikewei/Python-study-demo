#! /usr/bin/env python
# -*- coding=utf-8 -*-

"""
Created on 2018-10-22
解析到买卖判断的代理
@author: lkw
"""

import zmq


def main():
    try:
        context = zmq.Context(1)
        # Socket facing clients
        frontend = context.socket(zmq.PULL)
        frontend.bind("tcp://*:5555")

        # Socket facing services
        backend = context.socket(zmq.PUSH)
        backend.bind("tcp://*:5556")

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
