# coding=utf-8
'''
Created on 2015-10-10
你无法连续向服务器发送数据，必须发送一次，接收一次
REQ和REP模式中，客户端必须先发起请求
@author: kwsy2015
'''
import zmq

context = zmq.Context()
print('connect to hello world server')
socket = context.socket(zmq.REQ)
socket.connect('tcp://localhost:5555')

for request in range(1, 10):
    print('send ', request, '...')
    socket.send('hello')
    message = socket.recv()
    print('received reply ', request, '[', message, ']')
