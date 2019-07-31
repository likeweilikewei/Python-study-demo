#! /usr/bin/env python
# -*-coding=utf-8-*-

"""
描述符也是类，可以为其增加方法。比如增加回调方法，描述符是一个用来回调的很好的手段。
比如想要一个类的某个状态发生变化就立刻通知我们，可以自定义回调函数用来响应类中的状态变化。
如以下代码，
有木有感觉很厉害…__set__()方法感觉就像一个监督人员，监视属性的一举一动。
"""

from weakref import WeakKeyDictionary


class CallbackProperty(object):
    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self        
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):  # 每次改变值的时候都会调用low_balance_warning函数
        for callback in self.callbacks.get(instance, []):
            # alert callback function of new value
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """Add a new function to call every time the descriptor within instance updates"""
        if instance not in self.callbacks:
            self.callbacks[instance] = []  # 实例->[方法,]
        self.callbacks[instance].append(callback)


class BankAccount(object):
    balance = CallbackProperty(0)


def low_balance_warning(value):
    if value < 100:
        print("You are now poor")
    else:
        print('You are now rich!!!')


def check(value):
    print('You have %s money, Good Luck!!!' % value)

ba = BankAccount()
BankAccount.balance.add_callback(ba, low_balance_warning)
BankAccount.balance.add_callback(ba, check)

ba.balance = 5000                    # You are now rich!!!  You have 5000 money, Good Luck!!!
print("Balance is %s" % ba.balance)   # Balance is 5000
ba.balance = 99                      # You are now poor    You have 99 money, Good Luck!!!
print("Balance is %s" % ba.balance)   # Balance is 99
