#! /user/bin/env python
# -*- utf-8 -*-

import zmq
import sys
from tool import check
context = zmq.Context()

#  Socket to talk to server
print("Connecting to message server...")
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.RECONNECT_IVL,100)
socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)
socket.connect("tcp://localhost:5555")

socket_market = context.socket(zmq.REQ)
socket_market.connect("tcp://localhost:5556")

socket.setsockopt_string(zmq.SUBSCRIBE,'')  # 消息过滤

while True:
    response = socket.recv()
    response = check(response)
    if response:
        print('Part four received pol {} market query.'.format(response['id']))
        response['part'] = 'four'
        response['result'] = {'four': 'hello'}
        socket_market.send_json(response)
        response_market = socket_market.recv_json()
        print(response_market)
