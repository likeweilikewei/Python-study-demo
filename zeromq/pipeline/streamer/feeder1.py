#! /user/bin/env python
# -*- utf-8 -*-

import time
import zmq


class STest:
    def __init__(self):
        self.name = 'li'


def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.connect("tcp://127.0.0.1:5559")
    # Start your result manager and workers before you start your producers
    for num in range(20000):
        work_message = { 'num' : num}
        test = STest()
        zmq_socket.send_pyobj(test)
        # zmq_socket.send_json(work_message)
        time.sleep(1)
        print('sends obj:{}'.format(test))

if __name__ == '__main__':
    producer()
