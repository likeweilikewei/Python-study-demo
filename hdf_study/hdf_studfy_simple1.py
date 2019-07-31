#! /user/bin/env python
# -*- coding=utf-8 -*-


import pandas as pd
import numpy as np
import h5py

temperature = np.random.random(1024)
# print('temperature:{}'.format(temperature))

wind = np.random.random(2048)
dt_wind = 5

start_time = 1375204299
station = 15

f = h5py.File('weather.hdf5')
# f['/12/temperature'] = temperature
# f['/12/temperature'].attrs['dt'] = station
# f['/12/temperature'].attrs['start_time'] = start_time
#
# f['/16/wind'] = wind
# f['/16/wind'].attrs['dt'] = dt_wind

dataset = f['/12/temperature']
for key,value in dataset.attrs.items():
    print('{}:{}'.format(key,value))

for key1,value1 in f.items():
    print("{}:{}".format(key1,value1))

for i1 in dataset:
    print(i1)

# print(f)
# print(type(f))
#
# print(list(f.keys()))
# for key,value in f.items():
#     print(key,value)
#     print(type(key),type(value))

# dset = f['15']
# print(dset)
# print(type(dset))
# print(dset['temperature'])
# temperatures = dset['temperature']
# temperaturess = f['/15/temperature']
# print(temperaturess)
# print(temperaturess.shape)
# print(list(temperaturess))
# for i in temperaturess:
#     print(i)


# print(temperature.shape)

# for i in f.iteritems():
#     print(i)
