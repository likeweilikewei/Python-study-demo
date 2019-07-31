# coding=utf-8
'''
Created on 2015-10-10
回复请求
@author: kwsy2015

       1、 必须先提问，后回答

        2、 对于一个提问，只能回答一次

        3、 在没有收到回答前不能再次提问
'''
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind('tcp://*:5555')

while True:
    message = socket.recv()
    print('received request: ', message)

    time.sleep(1)
    socket.send('World')
