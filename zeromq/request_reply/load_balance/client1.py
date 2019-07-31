#! /user/bin/env python
# -*- utf-8 -*-

import zmq
# from zmq import zmq_setsockopt
print(zmq.__version__)

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.setsockopt(zmq.RECONNECT_IVL,100)
socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)

socket.connect("tcp://localhost:5555")
socket.connect("tcp://localhost:5556")
socket.connect("tcp://47.97.218.10:5557")
#  Do 10 requests, waiting each time for a response
for request in range(1,1000):
    print("Sending request ", request,"...")
    socket.send_string("Hello, {}".format(request))

    #  Get the reply.
    message = socket.recv()
    print("Received reply ", request, "[", message, "]")

# 关闭连接
socket.close()
