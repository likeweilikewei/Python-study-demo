#coding=utf-8
'''
Created on 2015-10-13
发起请求
@author: kwsy2015
'''
import zmq

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
#这一次，我们不连接REP，而是连接ROUTER，多个REP连接一个ROUTER
socket.connect("tcp://localhost:5559")

# 发送问题给ROUTER
for request in range(1,1000):
    print(1)
    socket.send_json({'id':request,'query':'query{}'.format(request),'info':'info{}'.format(request)})
    print(2)
    message = socket.recv()
    print(3)
    print("Received reply %s [%s]" % (request, message))
socket.close()
context.term()
