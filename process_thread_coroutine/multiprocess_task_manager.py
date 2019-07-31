#! /usr/bin/env python
# -*-coding=utf-8-*-
"""
这个简单的Manager/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，
就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。

Queue对象存储在哪？注意到taskworker.py中根本没有创建Queue的代码，所以，Queue对象存储在taskmanager.py进程中：

而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。

authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果taskworker.py的authkey和taskmanager.py的authkey不一致，肯定连接不上。

小结
Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。

注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，
就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
"""


# taskmanager.py

# 分布式: master
import random, queue
# managers子模块支持把多进程分布到多台机器上
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()


# 从BashManager继承
class QueueManager(BaseManager):
    pass


# 1. 把两个Queue都注册到网络上, callable关联queue对象
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def test():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 2. 绑定端口, 设置验证码
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 3. 启动Queue
    manager.start()

    # 4. 通过网络获得Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 5. 放置任务
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d...' % n)
        task.put(n)
    # 6. 获取结果
    print('Try get result...')
    for i in range(10):
        # r = result.get(timeout=10)
        r = result.get()
        print('Result: %s' % r)

    # 7. Close
    manager.shutdown()
    print('********* Master exit *********')

if __name__  == '__main__':
    test()
