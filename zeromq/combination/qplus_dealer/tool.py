# coding=utf-8


"""
零散的工具
"""


def check(message):
    """
    校验zmq的返回消息
    :param message:
    :return:
    """
    try:
        result = eval(message)
        if isinstance(result,dict):
            result = result
        else:
            result = {}
    except:
        result = {}
    return result
