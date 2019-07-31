#! /user/bin/env python
# -*- coding=utf-8 -*-

import redis
import pandas as pd
import numpy as np
from quant_backend.util.redisManager import *
from quant_backend.settings.settings import redisManager0

""""
测试keys
"""


def keys():
    """
    测试模糊查询keys
    :return:
    """
    _redis = redisManager0
    s = _redis.keys(name='rank:office:datb:[123]*')
    print(s)
keys()
