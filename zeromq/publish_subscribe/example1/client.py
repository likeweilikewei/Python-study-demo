# coding=utf-8
'''
Created on 2015-10-13
订阅模式，如果设置了过滤条件，那么只会接收到以过滤条件开头的消息
@author: kwsy2015
'''
import sys
import zmq
print(sys.argv)
import time

#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)

print("Collecting updates from weather server...")
socket.connect("tcp://localhost:5556")

# Subscribe to zipcode, default is NYC, 10001
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10002"

# 此处设置过滤条件，只有以 zip_filter 开头的消息才会被接收
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)

# Process 5 updates
total_temp = 0
for update_nbr in range(50):
    print(1)
    string = socket.recv()
    print(2)
    print(string)
    time.sleep(1)
    print(3)
    print(string)
    zipcode, temperature, relhumidity = string.split()
    print(zipcode, temperature, relhumidity)
    total_temp += int(temperature)
    print(4)

print("Average temperature for zipcode '%s' was %dF" % (
    zip_filter, total_temp / 5)
      )
