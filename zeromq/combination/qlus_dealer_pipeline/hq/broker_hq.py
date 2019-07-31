# coding=utf-8
"""
Created on 2018-10-26
@author:lkw
"""

import zmq

try:
    # Prepare our context and sockets
    contexts = zmq.Context()

    frontend = contexts.socket(zmq.ROUTER)
    backend = contexts.socket(zmq.DEALER)
    frontend.bind("tcp://*:5563")
    backend.bind("tcp://*:5564")

    # Initialize poll set
    poller = zmq.Poller()
    poller.register(frontend, zmq.POLLIN)
    poller.register(backend, zmq.POLLIN)
except Exception as e:
    print('error:',e)
    frontend.close()
    backend.close()
    contexts.term()


# Switch messages between sockets
while True:
    socks = dict(poller.poll())
    # frontend 收到了提问后，由backend发送给REP端
    if socks.get(frontend) == zmq.POLLIN:
        message = frontend.recv_multipart()
        backend.send_multipart(message)

    # backend 收到了回答后，由frontend发送给REQ端
    if socks.get(backend) == zmq.POLLIN:
        message = backend.recv_multipart()
        frontend.send_multipart(message)
