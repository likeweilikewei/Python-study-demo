# -*- coding=utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.connect("tcp://localhost:5556")
socket.setsockopt_string(zmq.SUBSCRIBE,"teresa")  # 消息过滤
socket.setsockopt_string(zmq.SUBSCRIBE,"like")  # 消息过滤
socket.setsockopt_string(zmq.SUBSCRIBE,"john")  # 消息过滤
socket.setsockopt_string(zmq.SUBSCRIBE,"tom")  # 消息过滤

while True:
    response = socket.recv()
    print("client 1 response: %s" % str(response,encoding='utf-8'))
