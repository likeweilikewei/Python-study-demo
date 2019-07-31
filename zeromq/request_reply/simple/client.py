# -*- coding=utf-8 -*-

import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# socket.send(b'Are you OK?')
# response = socket.recv()
# print("response: %s" % response)

# socket.send_json({'name':'li'})
# response_one = socket.recv_json()
# print("answer:{}".format(response_one))

#  发送问题给ROUTER
for request in range(1,1000):
    socket.send_json({'id':request,'query':'query{}'.format(request),'info':'info{}'.format(request)})
    message = socket.recv_json()
    print("Received reply %s [%s]" % (request, message))
socket.close()
