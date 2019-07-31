"""
 定义一个带参数的装饰器
 看起来，这种实现看上去很复杂，但是核心思想很简单。 最外层的函数 logged() 接受参数并将它们作用在内部的装饰器函数上面。
 内层的函数 decorate() 接受一个函数作为参数，然后在函数上面放置一个包装器。 这里的关键点是包装器是可以使用传递给 logged() 的参数的。

讨论
定义一个接受参数的包装器看上去比较复杂主要是因为底层的调用序列。特别的，如果你有下面这个代码：

@decorator(x, y, z)
def func(a, b):
    pass
装饰器处理过程跟下面的调用是等效的;

def func(a, b):
    pass
func = decorator(x, y, z)(func)
decorator(x, y, z) 的返回结果必须是一个可调用对象，它接受一个函数作为参数并包装它， 可以参考9.7小节中另外一个可接受参数的包装器例子。
"""

from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的
    functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate

"""
logged(logging.DEBUG)接收一个and作为参数，调用时候，add(),会先运行logged(logging.EDBUG)(add)返回一个可调用对象wrapper，
这时候add变成了这个新函数，调用add(),就是调用wrapper()
"""
# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')
