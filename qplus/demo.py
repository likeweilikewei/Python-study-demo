#coding=utf-8

import copy
import datetime
from collections import Iterable


class Symbol:
    def __init__(self, info, date=datetime.datetime.now()):
        # print(info)
        # print(type(info))
        if not isinstance(info, dict) and not isinstance(info,set):
            raise TypeError

        # code = set(dicts[info['plate']])
        self.__info = info
        self.__code = self.members(self.__info)
        self.__date = date

    @staticmethod
    def members(info):
        """
        选股
        :param info:
        :return:
        """
        dicts = {'000001.SH': ['000010', '000002', '000003', '000004', '000005'],
                 '000002.SH': ['000006', '000002', '000003', '000004', '000007'],
                 '399107.SZ': ['000001', '000011', '000006', '000004', '000005'],
                 '399105.SZ': ['000001', '000012', '000007', '000004', '000005'],
                 '399005.SZ': ['000001', '000013', '000008', '000004', '000005'],
                 '399006.SZ': ['000001', '000014', '000009', '000004', '000005'],
                 'ah001': ['000001', '000015', '000010', '000004', '000005'],
                 '000300.SH': ['000001', '000016', '000011', '000004', '000005'],
                 '000016.SH': ['000001', '000002', '000003', '000004', '000005'],

                 '000010.SH': ['000001', '000017', '000012', '000004', '000005'],
                 '000009.SH': ['000006', '000018', '000013', '000004', '000007'],
                 '399330.SZ': ['000001', '000019', '000014', '000004', '000005'],
                 '399007.SZ': ['000001', '000010', '000015', '000004', '000005'],
                 '399008.SZ': ['000001', '000011', '000016', '000004', '000005'],
                 '399903.SZ': ['000001', '000007', '000006', '000004', '000005'],
                 '000905.SH': ['000001', '000009', '000011', '000004', '000005'],
                 }
        if isinstance(info,dict):
            _code = set(dicts[info['index']])
        elif isinstance(info,set):
            _code = info
        else:
            _code = set([])
        return _code

    @property
    def code(self):
        return self.__code

    def __and__(self, other):
        return Symbol(self.code & other.code)

    def __or__(self, other):
        return Symbol(self.code | other.code)

    """
    左移位代表交集
    """
    def __lshift__(self, other):
        return Symbol(self.code & other.code)

    """
    右移位代表并集
    """
    def __rshift__(self, other):
        return Symbol(self.code | other.code)

    def __str__(self):
        return str(self.code)

    def __repr__(self):
        return str(self.code)

# s = traverse({
#     "left":[{
#         "left":[{"targetParamId" : "000001.SH",
#             "targetParamVal" : "profitEval.lossAdd.add(47.09)",
#             "targetScene" : "10303",
#             "unit" : "%",}],
#         "right":[{"targetParamId" : "000002.SH",
#             "targetParamVal" : "stkPkRng.indexStock(000016.SH)",
#             "targetScene" : "10307"}],
#         "op": ">>"}],
#     "right": [{
#         "left": [{"targetParamId": "399107.SZ",
#                   "targetParamVal": "profitEval.lossAdd.add(47.09)",
#                   "targetScene": "10303",
#                   "unit": "%", }],
#         "right": [{
#                     "left":[{"targetParamId" : "399105.SZ",
#                         "targetParamVal" : "profitEval.lossAdd.add(47.09)",
#                         "targetScene" : "10303",
#                         "unit" : "%",}],
#                     "right":[{"targetParamId" : "399005.SZ",
#                         "targetParamVal" : "stkPkRng.indexStock(000016.SH)",
#                         "targetScene" : "10307"}
#                              ],
#                     "op":">>"}],
#         "op":">>"
#     }],
#     "op":"<<"
# })
# print(s)
# print(type(s))

data = {'left':[{
            'left':[{'left':[{'000001.SH':1,'plate':'000001.SH'}],'right':[{'000002.SH':2,'plate':'b'}],'op':'>>'}],
            'right':[{
                'left':[{'399107.SZ':3,'plate':'399107.SZ'}],
                'right':[{
                    'left':[{'399105.SZ':4,'plate':'399105.SZ'}],
                    'right':[{'399005.SZ':5,'plate':'399005.SZ'}],
                    'op':'<<'}],
                'op':'>>'}],
            'op':'<<'}],
        'right':[{
            'left':[{
                'left':[{'399006.SZ':6,'plate':'399006.SZ'}],
                'right':[{'ah001':7,'plate':'ah001'}],
                'op':'<<'}],
            'right':[{
                'left':[{'000300.SH':8,'plate':'000300.SH'}],
                'right':[{'000016.SH':9,'plate':'000016.SH'}],
                'op':'<<'}],
            'op':'>>'}],
        'op':'>>'}
# ss = traverse(data)
# ss = ''.join(ss)
# print(ss)

# aList = [123, 'xyz', 'zara', 'abc']
#
# aList.insert( 10, 2009)
# print(aList)


class ParseJson:
    def __init__(self):
        self.__json = None
        self.__symbol_word = None
        self.li = None

    @property
    def json(self):
        return self.__json

    @json.setter
    def json(self,json_tmp):
        self.__json = json_tmp

    @property
    def symbol_word(self):
        return self.__symbol_word

    @staticmethod
    def json_to_symbol(_json_data:dict)->str:
        """
        json解析模块
        :param _json_data:
        :return:
        """
        print(_json_data)
        _result=[]

        def insert_next(_data:list,element:str,location:int)->int:
            """
            求元素的下个位置
            :param _data: 数据集
            :param element: 元素
            :param location: 默认位置
            :return:
            """
            if not isinstance(_data,list):
                raise Exception('求下个坐标的数据不是list')
            elif element not in _data:
                return location
            else:
                return _data.index(element)+1

        def traverse(json_data:dict, location=0, insert_flag=0)->list:
            """
            对json对象进行递归遍历，解析成加括号的形式
            :param json_data:
            :param location:
            :param insert_flag:
            :return:
            """
            # 递归遍历
            if isinstance(json_data, dict):
                # 如果数据开始就不是交并就直接输出
                if 'left' in json_data.keys():
                    # 如果left在数据中
                    if 'left' in json_data['left'][0].keys():
                        if insert_flag:
                            _result.insert(location, '(')
                            _result.insert(location, ')')
                            _result.insert(location, json_data['op'])
                            traverse(json_data['left'][0], location=location - 2, insert_flag=1)
                        else:
                            _result.append('(')
                            _result.append(')')
                            _result.append(json_data['op'])
                            traverse(json_data['left'][0], location=-2, insert_flag=1)
                    else:
                        _result.insert(location, 'Symbol({})'.format(json_data['left'][0]))
                        __index = _result.index('Symbol({})'.format(json_data['left'][0]))
                        _result.insert(__index+1,json_data['op'])

                    # 如果right在数据中
                    if 'right' in json_data['right'][0].keys():
                        if insert_flag:
                            _result.insert(location, '(')
                            _result.insert(location, ')')
                            traverse(json_data['right'][0], location=location - 1, insert_flag=1)
                        else:
                            _result.append('(')
                            _result.append(')')
                            traverse(json_data['right'][0], location=-1, insert_flag=1)
                    else:
                        _result.insert(location, 'Symbol({})'.format(json_data['right'][0]))
                else:
                    return 'Symbol({})'.format(json_data)
            else:
                raise Exception("data is not dict.")
            return _result
        symbol_word = ''.join(traverse(json_data=_json_data))
        return symbol_word

    def translate(self):
        """
        执行json的转化
        :return:
        """
        # print(self.__dict__['li'])
        # print(self.__dict__['json'])
        # print(self.__dict__)
        # print(self)
        self.__symbol_word = self.json_to_symbol(_json_data=self.__json)
        return self.symbol_word

    def __repr__(self):
        return str(self.symbol_word)

    def __str__(self):
        return str(self.symbol_word)


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        for __key,__value in attr.items():
            if hasattr(obj,__key):
                setattr(obj,__key,__value)
            else:
                obj.__dict__.update({__key:__value})
        return obj

if __name__ == '__main__':
    # statement = """Symbol({"index":"000001.SH"}) << (Symbol({"index":"000002.SH"}) >> Symbol({"index":"399107.SZ"}))"""
    # result = eval(statement)
    # print(result)

    # user = ParseJson()
    # user.json_to_symbol()
    # user.exec_symbol()

    data_1 = {'left':[{'index':'000001.SH'}],
              'right':[{
                  'left':[{'index':'000002.SH'}],
                  'right':[{'index':'399107.SZ'}],
                  'op':'>>'}],
              'op':'<<'}

    data_2 = {'left':[{
            'left':[{
                'left':[{'000001.SH':1,'index':'000001.SH'}],
                'right':[{'000002.SH':2,'index':'000002.SH'}],
                'op':'>>'}],
            'right':[{
                'left':[{'399107.SZ':3,'index':'399107.SZ'}],
                'right':[{
                    'left':[{'399105.SZ':4,'index':'399105.SZ'}],
                    'right':[{'399005.SZ':5,'index':'399005.SZ'}],
                    'op':'<<'}],
                'op':'>>'}],
            'op':'<<'}],
        'right':[{
            'left':[{
                'left':[{'399006.SZ':6,'index':'399006.SZ'}],
                'right':[{'ah001':7,'index':'ah001'}],
                'op':'<<'}],
            'right':[{
                'left':[{'000300.SH':8,'index':'000300.SH'}],
                'right':[{'000016.SH':9,'index':'000016.SH'}],
                'op':'<<'}],
            'op':'>>'}],
        'op':'>>'}
    parse = ParseJson()
    prototype = Prototype()
    prototype.register_object('parse', parse)
    parser = prototype.clone('parse', json=data_2,li=2)
    # print(parser)
    json_data_tmp = parser.translate()
    print(json_data_tmp)
    result = eval(json_data_tmp)
    print(result)
