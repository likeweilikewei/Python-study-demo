# -*- coding=utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5557")
socket.connect("tcp://localhost:5556")
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE,"like")  # 消息过滤
socket.setsockopt_string(zmq.SUBSCRIBE,"john")  # 消息过滤

while True:
    response = socket.recv()
    print("client 3 response: %s" % response.decode('utf-8'))
