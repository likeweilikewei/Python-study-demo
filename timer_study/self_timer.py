#! /user/bin/env python
# -*- coding=utf-8 -*-

import threading
import time


class Pysettimer(threading.Thread):
    '''
    Pysettimer is simulate the C++ settimer ,
    it need  pass funciton pionter into the class ,
    timeout and is_loop could be default , or customized
    '''

    def __init__(self, function, args=None, timeout=1, is_loop=False):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        # inherent the funciton and args
        self.function = function
        self.args = args  # pass a tuple into the class
        self.timeout = timeout
        self.is_loop = is_loop

    def run(self):
        while not self.event.is_set():
            self.event.wait(self.timeout)  # wait until the time eclipse

            self.function(self.args)

            if not self.is_loop:
                self.event.set()

    def stop(self):
        self.event.set()


def functest(args):
    print('hello world ， this is ' , args[0])


def main():
    mytime = Pysettimer(functest, ('python ', 'program '))
    # multiple ,dynamic argument wouldnot affect  Pysettimer class API port

    mytime.start()

    time.sleep(10)  # append the main thread
    mytime.stop()  # end the timer thread .
    print('time over')


if __name__ == '__main__':
    main()


