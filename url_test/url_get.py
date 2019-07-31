#! /user/bin/env python
# -*- coding=utf-8 -*-


import requests


def test_1():
    """
    注意最后的/不能少
    :return:
    """
    url = 'https://stocks.root.com/index_block_filter/'
    params = {'indication': 'nMatch,riseAndFallRate', 'range_type': 'B,A', 'range_value': '10;2,10',
              'page': 1, 'pagesize': 10, 'indication_type': 2}
    r = requests.get(url, params=params)
    """
    如果不加这一句，返回的是一个response对象
    <Response [200]>
    <class 'requests.models.Response'>
    """
    r = r.json()
    print(r)
    print(type(r))
test_1()
