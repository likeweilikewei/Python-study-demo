#! /user/bin/env python
# -*- utf-8 -*-

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to message server...")
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.RECONNECT_IVL,100)
socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)

socket.connect("tcp://localhost:5555")
socket.connect("tcp://localhost:5556")
socket.connect("tcp://localhost:5557")
socket.connect("tcp://localhost:5558")

socket.setsockopt_string(zmq.SUBSCRIBE,"market")  # 消息过滤

while True:
    response = socket.recv()
    print('Part four received message:{}'.format(str(response,encoding='utf-8')))
