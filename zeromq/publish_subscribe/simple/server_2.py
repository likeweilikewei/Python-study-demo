# -*- coding=utf-8 -*-
import zmq
import time
import random
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")


while True:
    print('发送age {}'.format(datetime.now()))
    socket.send_string('{} age:{}'.format('john',random.randint(10,20)))
    time.sleep(2)
