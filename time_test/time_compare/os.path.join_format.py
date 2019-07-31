#! /usr/bin/env python
# -*-coding=utf-8-*-

import os
import time


def test_1():
    project_path = os.path.dirname(__file__)
    time1 = time.time()
    paths = os.path.join(project_path, 'data/test1')
    time2 = time.time()
    path2 = project_path + '/data/test1'
    print(path2)
    time3 = time.time()
    timea = time2-time1
    timeb = time3-time2
    print('join: {}\nformat: {}'.format(timea, timeb))
test_1()
