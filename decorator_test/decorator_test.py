#! /usr/bin/env python
# -*-coding=utf-8-*-

"""
url:http://python.jobbole.com/86632/
url:https://www.zhihu.com/question/26930016
"""
import os
import traceback
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from logging.handlers import TimedRotatingFileHandler

"""
os.path.dirname：返回文件的路径
__file__：指向当前的文件名
os.path.pardir：返回当前文件的父目录的路径
abspath:返回绝对路径，
os.path.dirname(__file__): D:/jiuniu chat/jiuniu_robot_lsi_class/tests/decorator_test
os.path.pardir: ..
os.path.join(os.path.dirname(__file__), os.path.pardir): D:/jiuniu chat/jiuniu_robot_lsi_class/tests/decorator_test\..
os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)): D:\jiuniu chat\jiuniu_robot_lsi_class\tests
root path: D:\jiuniu chat\jiuniu_robot_lsi_class\tests
project path: D:\jiuniu chat\jiuniu_robot_lsi_class\tests\decorator_test
log path: D:\jiuniu chat\jiuniu_robot_lsi_class\tests\decorator_test\log\test_log
"""
class Logging:
    def __init__(self, _log_path_name):
        self.__log_path_name = _log_path_name

    def __call__(self, func):
        self.func = func

        def real_func(*args, **kwargs):
            # dirname：返回文件的路径，pardir:返回当前文件的父目录的表示，通常是.., __file__指向当前的文件名
            # 因此os.path.dirname(__file__), os.path.pardir)返回父目录的路径，abspath返回绝对路径。
            # print('os.path.dirname：返回文件的路径\n__file__：指向当前的文件名\nos.path.pardir：返回当前文件的父目录\
            #       的路径\nabspath:返回绝对路径，\nos.path.dirname(__file__): {}\nos.path.pardir: {}\n\
            #       os.path.join(os.path.dirname(__file__), os.path.pardir): {}\nos.path.abspath(os.path.join(os.path.\
            #       dirname(__file__), os.path.pardir)): {}'.format(os.path.dirname(__file__),
            #                                                       os.path.pardir,
            #                                                       os.path.join(os.path.dirname(__file__), os.path.pardir),
            #                                                       os.path.abspath(
            #                                                           os.path.join(os.path.dirname(__file__),
            #                                                                        os.path.pardir))))
            ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
            # print('root path: {}'.format(ROOT_PATH))
            # 返回当前的项目目录, 这个jiuniu_robot_lsi_class在上传的时候改为robot
            PROJECT_PATH = os.path.join(ROOT_PATH, 'decorator_test')
            # print('project path: {}'.format(PROJECT_PATH))
            # 普通的全部运行日志
            log_file_path = os.path.join(PROJECT_PATH, 'log', self.__log_path_name)
            # print('log path: {}'.format(log_file_path))

            # log_file_path = self.__log_path_name  # 日志按日期滚动，保留5天
            logger_decorator = logging.getLogger()
            logger_decorator.setLevel(logging.INFO)
            """用于写入日志"""
            handler_decorator = TimedRotatingFileHandler(log_file_path,
                                                         when="d",
                                                         interval=1,
                                                         backupCount=5)
            """再创建一个handler，用于输出到控制台"""
            handler_out = logging.StreamHandler()
            handler_out.setLevel(logging.DEBUG)

            """定义handler的格式"""
            formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
            handler_decorator.setFormatter(formatter)
            handler_out.setFormatter(formatter)

            """给logger添加handler"""
            logger_decorator.addHandler(handler_decorator)
            logger_decorator.addHandler(handler_out)

            """如果能顺利运行就日志记录运行的参数和结果，如果不能就返回错误的日志"""
            try:
                print(1)
                logger_decorator.info("Arguments were: %s, %s" % (args, kwargs))
                _result = func(*args, **kwargs)
                logger_decorator.info(result)
                print(2)
            except:
                logger_decorator.error(traceback.format_exc()+'\n')
                # logger_decorator.info(e)  # e只有错误原因，上述的traceback有出错的路径
        return real_func


@Logging('test_log')
def test_1(number1):
    number_tmp = number1
    result = 10 / number_tmp
    print(3)
    print('results: {}'.format(result+1+2))
    return result

# 执行顺序：1 3 2
# test_1(1)
# test_1(number1=0)
# print(os.path.dirname(__file__))


class LoggingEmail:
    def __init__(self, _log_path_name):
        self.__log_path_name = _log_path_name

    def __call__(self, func):
        self.func = func

        def real_func(*args, **kwargs):
            flag, message, _result = self.log(func=func, arg=args, kwarg=kwargs)
            if not flag:
                self.email(message=message)
            return _result
        return real_func

    def log(self, func, arg, kwarg):
        project_path = os.path.dirname(__file__)
        log_file_path = os.path.join(project_path, 'log', self.__log_path_name)
        logger_decorator = logging.getLogger()
        logger_decorator.setLevel(logging.INFO)
        """创建一个handler,用于写入日志"""
        handler_decorator = TimedRotatingFileHandler(log_file_path,
                                                     when="d",
                                                     interval=1,
                                                     backupCount=5)
        """再创建一个handler，用于输出到控制台"""
        handler_out = logging.StreamHandler()
        handler_out.setLevel(logging.DEBUG)

        """定义handler的格式"""
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        handler_decorator.setFormatter(formatter)
        handler_out.setFormatter(formatter)

        """给logger添加handler"""
        logger_decorator.addHandler(handler_decorator)
        logger_decorator.addHandler(handler_out)

        """记录日志"""
        try:
            logger_decorator.info("running function: %s\nArguments were: %s, %s" % (func.__name__, arg, kwarg))
            _result = func(*arg, **kwarg)
            """如果没有return,则返回为None"""
            logger_decorator.info(_result)
            return True, None, _result
        except:
            message = 'function {} running error: {}'.format(func.__name__, traceback.format_exc()) + '\n'
            logger_decorator.error(message)
            return False, message, 'ResultError'

    @staticmethod
    def email(message):
        my_sender = '123456@qq.com'  # 发件人邮箱账号
        my_pass = '123456'  # 发件人邮箱密码
        my_user = '123456@qq.com'  # 收件人邮箱账号，我这边发送给自己

        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = formataddr(["罗伯特·德尼罗", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["罗伯特·德尼罗", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "聊天神器运行出错"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接


class Test:
    @LoggingEmail('test_2_log')
    def test_2(self, number1):
        number_tmp = number1
        _result = 10 / number_tmp
        return _result

tests = Test()
results = tests.test_2(number1=0)
print('result: {}'.format(results))

