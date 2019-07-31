#! /user/bin/env python
# -*- coding=utf-8 -*-


"""
contextmanager可以用来创建上下文管理器，
在数年前，Python 2.5 加入了一个非常特殊的关键字，就是with。with语句允许开发者创建上下文管理器。
什么是上下文管理器？上下文管理器就是允许你可以自动地开始和结束一些事情。
例如，你可能想要打开一个文件，然后写入一些内容，最后再关闭文件。这或许就是上下文管理器中一个最经典的示例。
事实上，当你利用with语句打开一个文件时，Python替你自动创建了一个上下文管理器。
https://www.cnblogs.com/zhbzz2007/p/6158125.html

Python 2.5 不仅仅添加了with语句，它也添加了contextlib模块。
这就允许我们使用contextlib的contextmanager函数作为装饰器，来创建一个上下文管理器。
让我们尝试着用它来创建一个上下文管理器，用于打开和关闭文件。
"""

from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path,"w")
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print("Closing file")
        f_obj.close()

if __name__ == "__main__":
    with file_open("./test.txt") as fobj:
        fobj.write("Testing context managers")
