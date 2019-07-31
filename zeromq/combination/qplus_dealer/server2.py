#coding=utf-8
'''
Created on 2015-10-13
收到请求后回复world
@author: kwsy2015
'''
import zmq
import time
from tool import check

context = zmq.Context()
socket = context.socket(zmq.REP)
# REP连接的是DEALER
socket.connect("tcp://localhost:5560")

while True:
    message = socket.recv_json()
    message = check(message)
    if message:
        print("Received pol {} deal request ...".format(message['id'],message))
        time.sleep(1.5)
        message['deal_flag'] = 1
        message['deal_info'] = {'sell':{'000001':{'price':12,'number':200}},'buy':{'390010':{'price':32.56,'number':650}}}
        socket.send_json(message)
        print('deal pol {} done.'.format(message['id']))
