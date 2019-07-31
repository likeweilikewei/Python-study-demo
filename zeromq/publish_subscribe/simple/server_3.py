# -*- coding=utf-8 -*-
import zmq
import time
import random
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5557")


while True:
    print('发送score {}'.format(datetime.now()))
    socket.send_string('{} score:{}'.format('tom',random.uniform(0,100)))
    time.sleep(2)
