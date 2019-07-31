class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)
#@后面跟的意味着可以接收一个func作为参数，返回一个可调用对象，调用这个可调用对象时候会在里面调用func，并且返回func的结果
@Counter
def foo():
    pass

def a():
    pass

for i in range(10):
    #这时候函数成了实例，调用函数就是调用这个实例对象，从而会调用__call__
    foo()

print(type(foo))
print(type(Counter))
print(type(Counter(a)))
print(foo.count)  # 10
