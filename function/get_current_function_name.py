#!/usr/bin/env python
# -*-coding=utf-8-*-

import inspect
import time


def get_current_function_name():
    """
    从内部获取函数名
    :return: 函数名
    """
    return inspect.stack()[1][3]


class MyClasses:
    def function_one(self):
        # print(get_current_function_name())
        # print("%s.%s ******" % (slf.__class__.__name__, get_current_function_name()))
        print(type(self.__class__.__name__))
        return get_current_function_name()

if __name__ == "__main__":
    time1 = time.time()
    myclass = MyClasses()
    result = myclass.function_one()
    time2 = time.time()
    print(time2 - time1)
