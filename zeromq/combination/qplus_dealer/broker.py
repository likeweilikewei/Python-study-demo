# coding=utf-8
'''
Created on 2015-10-13

@author: kwsy2015
'''
import zmq
from tool import check

# Prepare our context and sockets
context = zmq.Context()
frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

# 发布行情请求
context = zmq.Context()
socket = context.socket(zmq.PUB)
# socket.setsockopt(zmq.RECONNECT_IVL,100)
# socket.setsockopt(zmq.RECONNECT_IVL_MAX,500)
socket.bind("tcp://*:5555")

# 收集行情结果
contexts = zmq.Context()
socket_market = contexts.socket(zmq.REP)
socket_market.bind("tcp://*:5556")

# Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

# Switch messages between sockets
market = {}

while True:
    print(-2)
    socks = dict(poller.poll())
    print(-1)
    if socks.get(frontend) == zmq.POLLIN:
        print(1)
        result_tmp = frontend.recv_multipart()
        print(2)
        print('result:{}'.format(result_tmp))
        frontend.send(b'world')
        print(3)

    # print(1)
    # socks = dict(poller.poll())
    # # frontend 收到了提问后，由backend发送给REP端
    # if socks.get(frontend) == zmq.POLLIN:
    #     result_tmp = frontend.recv_multipart()
    #     print(2)
    #     result = check(result_tmp)
    #     if result:
    #         # 通过订阅模式广播行情请求
    #         print('收到策略请求：{}'.format(result))
    #         socket.send_json(result)
    #     else:
    #         print(result)
    #         continue
    #     print(3)
    #     # frontend.send(b'success')
    #
    # # 收集结果
    # market_tmp = socket_market.recv_json()
    # print(4)
    # market_tmp = check(market_tmp)
    # print(market_tmp)
    # socket_market.send_json(market_tmp)
    # print(5)
    # frontend.send(b'namessss')
    # print(6)
    #
    # # 当有数据的时候
    # if market_tmp:
    #     __id = market_tmp['id']
    #     __query = market_tmp['query']
    #     __result = market_tmp['result']
    #     __part = market_tmp['part']
    #     __info = market_tmp['info']
    #     if __id not in market.keys():
    #         market[__id] = {'{}'.format(__part):__result,'query':__query,'info':__info,'id':__id}
    #     elif __part not in market[__id].keys():
    #         market[__query]['{}'.format(__part)] = __result
    #     else:
    #         pass
    #
    # # 判断是否收集好了,通过经销商发给策略模块进行买卖判断
    # if len(market[__id]) == 7:
    #     print('策略 {} 收集好了：{}'.format(__id,market[__id]))
    #     backend.send_json(market[__id])
    #
    # # backend 收到了回答后，由frontend发送给REQ端
    # if socks.get(backend) == zmq.POLLIN:
    #     message = backend.recv_json()
    #     print('策略 {} 处理成功.'.format(message[__id]))
    #     frontend.send_json(message)
