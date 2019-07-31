# -*- coding: utf-8 -*-
from threading import Thread
import time


class TimeoutException(Exception):
    pass


ThreadStop = Thread._Thread__stop


def timelimited(timeout):
    def decorator(function):
        def decorator2(*args, **kwargs):
            class TimeLimited(Thread):
                def __init__(self, _error=None, ):
                    Thread.__init__(self)
                    self._error = _error

                def run(self):
                    try:
                        self.result = function(*args, **kwargs)
                    except Exception as e:
                        self._error = str(e)

                def _stop(self):
                    if self.isAlive():
                        ThreadStop(self)

            t = TimeLimited()
            t.start()
            t.join(timeout)

            if isinstance(t._error, TimeoutException):
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t.isAlive():
                t._stop()
                raise TimeoutException('timeout for %s' % (repr(function)))

            if t._error is None:
                return t.result

        return decorator2

    return decorator


@timelimited(2)  # 设置运行超时时间2S
def fn_1(secs):
    time.sleep(secs)
    return 'Finished without timeout'


def do_something_after_timeout():
    print('Time out!')


if __name__ == "__main__":
    try:
        print(fn_1(3))  # 设置函数执行3S
    except TimeoutException as e:
        print(str(e))
        do_something_after_timeout()
