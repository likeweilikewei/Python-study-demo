# coding=utf-8
'''
Created on 2015-10-13
@author: kwsy2015
'''
import zmq

# Prepare our context and sockets
context = zmq.Context()

frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

# Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

# Switch messages between sockets
while True:
    print(1)
    print(poller)
    if poller.poll():
        print('yes')
    else:
        print('no')
    print(poller.poll())
    socks = dict(poller.poll())
    print(2)
    print('socks:{}'.format(socks))
    print('backend:{}'.format(backend))
    print('socks.get backend:{}'.format(socks.get(backend)))
    print('zmq:{}'.format(zmq))
    print('zmq.POLLIN:{}'.format(zmq.POLLIN))
    # frontend 收到了提问后，由backend发送给REP端
    if socks.get(frontend) == zmq.POLLIN:
        print('socks:{}'.format(socks))
        print('backend:{}'.format(backend))
        print('socks.get backend:{}'.format(socks.get(backend)))
        print('zmq:{}'.format(zmq))
        print('zmq.POLLIN:{}'.format(zmq.POLLIN))
        print(3)
        message = frontend.recv_multipart()
        print(message)
        print(4)
        backend.send_multipart(message)
        print(5)

    # backend 收到了回答后，由frontend发送给REQ端
    print(6)
    if socks.get(backend) == zmq.POLLIN:
        print('socks:{}'.format(socks))
        print('backend:{}'.format(backend))
        print('socks.get backend:{}'.format(socks.get(backend)))
        print('zmq:{}'.format(zmq))
        print('zmq.POLLIN:{}'.format(zmq.POLLIN))
        message = backend.recv_multipart()
        print(message)
        print(7)
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # [b'\x00\x80\x00\x00*', b'', b'World server']
        # frontend.send_multipart([b'\x00\x80\x00\x00*', b'', b'World server'])
        frontend.send_multipart(message)
        print(8)
