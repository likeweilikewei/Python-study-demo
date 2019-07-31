#! /user/bin/env python
# -*- utf-8 -*-

import zmq
from tool import check

#  Socket to talk to server
context = zmq.Context()
print("Connecting to message server...")
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.RECONNECT_IVL,100)
socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)
socket.connect("tcp://localhost:5555")

socket_market = context.socket(zmq.REQ)
socket_market.connect("tcp://localhost:5556")

socket.setsockopt_string(zmq.SUBSCRIBE,'')  # 消息过滤,必须要有

while True:
    print('1')
    response = socket.recv()
    print('2')
    response = check(response)
    print('3')
    print(response)
    if response:
        print('4')
        print('Part one received pol {} market query.'.format(response['id']))
        response['part'] = 'one'
        response['result'] = {'one':'hello'}
        print('5')
        socket_market.send_json(response)
        print(6)
        response_market = socket_market.recv_json()
        print(response_market)
        print('7')
