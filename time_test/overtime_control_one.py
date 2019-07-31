# coding=utf-8
import signal
import time


"""
电脑系统是win10 64位，在使用python的signal模块时报错：“AttributeError: module 'signal' has no attribute 'SIGALRM'”，这是因为signal模块可以在linux下正常使用，但在windows下却有一些限制，在python文档https://docs.python.org/2/library/signal.html#signal.signal找到了如下解释：

"On Windows, signal() can only be called with SIGABRT, SIGFPE, SIGILL, SIGINT, SIGSEGV, or SIGTERM. A ValueError will be raised in any other case."

也就是说在windows下只能使用这几个信号：

SIGABRT
SIGFPE
SIGILL
SIGINT
SIGSEGV
SIGTERM

实际项目中会涉及到需要对有些函数的响应时间做一些限制，如果超时就退出函数的执行，停止等待。

可以利用python中的装饰器实现对函数执行时间的控制。

python装饰器简单来说可以在不改变某个函数内部实现和原来调用方式的前提下对该函数增加一些附件的功能，提供了对该函数功能的扩展。

方法一中使用的signal有所限制，需要在linux系统上，并且需要在主线程中使用。方法二使用线程计时，不受此限制。
"""


def set_timeout(num, callback):
    def wrap(func):
        def handle(signum, frame):  # 收到信号 SIGALRM 后的回调函数，第一个参数是信号的数字，第二个参数是the interrupted stack frame.
            raise RuntimeError

        def to_do(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handle)  # 设置信号和回调函数
                signal.alarm(num)  # 设置 num 秒的闹钟
                print('start alarm signal.')
                r = func(*args, **kwargs)
                print('close alarm signal.')
                signal.alarm(0)  # 关闭闹钟
                return r
            except RuntimeError as e:
                callback()

        return to_do

    return wrap


def after_timeout():  # 超时后的处理函数
    print("Time out!")


@set_timeout(2, after_timeout)  # 限时 2 秒超时
def connect():  # 要执行的函数
    time.sleep(3)  # 函数执行时间，写大于2的值，可测试超时
    print('Finished without timeout.')


if __name__ == '__main__':
    connect()
