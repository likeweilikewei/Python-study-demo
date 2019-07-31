# -*- coding=utf-8 -*-
import zmq
import time
import random
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

names = ['like','tom','john','teresa']

while True:
    print('发送name {}'.format(datetime.now()))
    socket.send_string('{} name: {}'.format(random.choice(names),random.choice(names)))
    time.sleep(2)
