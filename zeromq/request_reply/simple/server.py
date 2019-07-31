# -*- coding=utf-8 -*-
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_json()
    print("Received: %s" % message)
    # socket.send(b"I am OK!")
    socket.send_json({'result':'hello world.'})
