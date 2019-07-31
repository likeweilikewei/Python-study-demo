#! /user/bin/env python
# -*- coding=utf-8 -*-


import requests
import time
import hashlib
import json


# url = 'http://127.0.0.1:5002/questions'
# params = {'question': '一线龙头有哪些股票'}
#
# r = requests.get(url, params=params)
# r = r.json()
# print(r)

# url2 = 'http://127.0.0.1/api/robot/realtime/range/ranking'
# params = {'num': '10', 'type': '14901', 'range_type': 'B', 'indication': 'riseAndFallRate', 'range': '0', 'likewei:': 'hanggongxia'}
# r = requests.get(url2, params=params)
# r = r.json()
# print(r)

# type_list = []
# params = {}
# params['type'] = ','.join(type_list)
# print(params)
#
# if params['type']:
#     print(0)
# else:
#     print('妹纸')

t = time.time()
print(int(round(t * 1000)))    # 毫秒级时间戳
timestamp_1 = int(round(t * 1000))


hl = hashlib.md5()
# hl.update(string.encode(encoding='utf-8'))
sign = hl.hexdigest()
print(sign)

dict_small = {"input_type": int(1), "text": "我叫李可威"}
json_small = json.dumps(dict_small)
dicts = {"data": json_small, "data_type": "stt"}
rq = json.dumps(dicts)
print(type(rq))
# {"data": {"input_type": 1, "text": "我叫李可威"}, "data_type": "stt"}
url2 = 'https://cn.olami.ai/cloudservice/api'
texts = 'hello'
text = texts.encode(encoding='utf-8')
print(text)
params = {'appkey': str(appkey), 'api': str(api),
          'sign': str(sign),
          'timestamp': int(1517992769393),
          'rq': rq}
paramss = json.dumps(params)
print(paramss)
print(type(paramss))
r = requests.get(url2, params=params)
r = r.json()
print(r)


