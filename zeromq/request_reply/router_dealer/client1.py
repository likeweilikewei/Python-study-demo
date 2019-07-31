# coding=utf-8
'''
Created on 2015-10-13
发起请求
@author: kwsy2015
'''
import zmq
import time

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
# 这一次，我们不连接REP，而是连接ROUTER，多个REP连接一个ROUTER
socket.connect("tcp://localhost:5559")

#  发送问题给ROUTER
print(1)
for request in range(1, 11):
    print(2)
    socket.send(b"Hello aaaaaa")
    print(3)
    message = socket.recv()
    time.sleep(1)
    print(4)
    print("Received reply %s [%s]" % (request, message))
print(5)
socket.close()
context.term()
