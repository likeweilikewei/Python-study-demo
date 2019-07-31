#! /user/bin/env python
# -*- utf-8 -*-


import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.setsockopt(zmq.RECONNECT_IVL,100)
socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)
socket.bind("tcp://*:5556")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request server2: ", message)

    #  Do some 'work'
    time.sleep(1.5)  # Do some 'work'

    #  Send reply back to client
    socket.send_string("World")
