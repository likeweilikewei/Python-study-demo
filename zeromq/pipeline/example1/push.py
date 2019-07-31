# coding=utf-8
'''
Created on 2015-10-29
@author: kwsy2015
'''
import zmq
import time

context = zmq.Context()
server = context.socket(zmq.PUSH)
server.bind('tcp://*:6666')
count = 0
while True:
    server.send_string('%d' % count)
    print('send', 'count')
    count += 1
    time.sleep(0.2)
