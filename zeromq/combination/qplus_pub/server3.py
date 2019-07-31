#! /user/bin/env python
# -*- utf-8 -*-

import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.RECONNECT_IVL,100)
socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)
socket.bind("tcp://*:5557")

for i in range(2000,3000):
    socket.send_string('market request {}'.format(i))
    print('Sending request {} message ...'.format(i))
    time.sleep(1.5)
