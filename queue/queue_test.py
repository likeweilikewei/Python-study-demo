#! /user/bin/env python
# -*- coding=utf-8 -*-

import queue


def test_queue():
    q = queue.Queue()
    q.put(('pe', 1))
    x = q.get()
    print(x)
test_queue()
