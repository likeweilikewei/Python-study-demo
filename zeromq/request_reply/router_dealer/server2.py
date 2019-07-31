# coding=utf-8
'''
Created on 2015-10-13
收到请求后回复world
@author: kwsy2015
'''
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
# REP连接的是DEALER
socket.connect("tcp://localhost:5560")

print(1)
while True:
    print(2)
    message = socket.recv()
    print(3)
    print("Received request: %s" % message)
    socket.send_string("World serve {}".format(message))
    print(4)
