# coding=utf-8
'''
Created on 2015-10-29
@author: kwsy2015
'''
import zmq

context = zmq.Context()
client = context.socket(zmq.PULL)
client.connect('tcp://localhost:6666')
client.connect('tcp://localhost:6667')

while True:
    msg = client.recv()
    print(msg)
