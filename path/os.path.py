#! /usr/bin/env python
# -*-coding=utf-8-*-

"""
url:http://python.jobbole.com/86632/
url:https://www.zhihu.com/question/26930016
"""
import os
import traceback
import logging
from logging.handlers import TimedRotatingFileHandler
from gensim import models

"""
os.path.dirname：返回文件的路径
__file__：指向当前的文件名
os.path.pardir：返回当前文件的父目录的表示，通常是..
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
            print('os.path.dirname：返回文件的路径\n__file__：指向当前的文件名\nos.path.pardir：返回当前文件的父目录的父目录\
                  的路径\nabspath:返回绝对路径，\nos.path.dirname(__file__): {}\nos.path.pardir: {}\n\
                  os.path.join(os.path.dirname(__file__), os.path.pardir): {}\nos.path.abspath(os.path.join(os.path.\
                  dirname(__file__), os.path.pardir)): {}'.format(os.path.dirname(__file__),
                                                                  os.path.pardir,
                                                                  os.path.join(os.path.dirname(__file__), os.path.pardir),
                                                                  os.path.abspath(
                                                                      os.path.join(os.path.dirname(__file__),
                                                                                   os.path.pardir))))
            ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
            print('root path: {}'.format(ROOT_PATH))
            # 返回当前的项目目录, 这个jiuniu_robot_lsi_class在上传的时候改为robot
            PROJECT_PATH = os.path.join(ROOT_PATH, 'decorator_test')
            print('project path: {}'.format(PROJECT_PATH))
            # 普通的全部运行日志
            log_file_path = os.path.join(PROJECT_PATH, 'log', self.__log_path_name)
            print('log path: {}'.format(log_file_path))

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
            # logger_decorator.addHandler(handler_out)

            """如果能顺利运行就日志记录运行的参数和结果，如果不能就返回错误的日志"""
            try:
                logger_decorator.info("Arguments were: %s, %s" % (args, kwargs))
                result = func(*args, **kwargs)
                logger_decorator.info(result)
            except:
                logger_decorator.error(traceback.format_exc()+'\n')
                # logger_decorator.info(e)  # e只有错误原因，上述的traceback有出错的路径
        return real_func


@Logging('test_log')
def test_1(number1):
    number_tmp = number1
    results = 10 / number_tmp
    print('results: {}'.format(results))
    return results

# test_1(1)
# test_1(number1=0)


"""
python中os.path常用模块
__file__: 指向当前的文件名
os.path.sep: 路径分隔符 linux下就用这个了’/’
os.path.altsep: 根目录
os.path.curdir: 当前目录
os.path.pardir：父目录
os.path.abspath(path)：绝对路径
os.path.join(): 常用来链接路径
os.path.split(path): 把path分为目录和文件两个部分，以列表返回
os.path.dirname()：去掉脚本的文件名，返回目录。
"""


def test_2():
    print('os.path.sep: {}\nos.path.altsep: {}\nos.path.curdir: {}\nos.path.pardir: {}\nos.path.abspath(__file__): {}'.
          format(os.path.sep, os.path.altsep, os.path.curdir, os.path.pardir, os.path.abspath(__file__)))
    print('os.path.join(os.path.curdir, "likewei"): {}'.format(os.path.join(os.path.curdir, "likewei")))
    print('os.path.split(os.path.abspath(__file__)): {}'.format(os.path.split(os.path.abspath(__file__))))
    print('os.path.dirname(__file__): {}'.format(os.path.dirname(__file__)))  # 返回当前文件所在目录的路径

# test_2()


def test_3():
    """
    多层路径相加时候用一下两种方法都可以。

    tests_path: D:/jiuniu chat/jiuniu_robot_lsi_class/tests/path\likewei
    成功加载：Dictionary(4245 unique tokens: ['不低于', '不低过', '不多于', '不大于', '不小于']...)
    D:/jiuniu chat/jiuniu_robot_lsi_class/tests/path\likewei\BigClassDictionary
    type path: <class 'str'>
    成功加载：Dictionary(4245 unique tokens: ['不低于', '不低过', '不多于', '不大于', '不小于']...)
    D:/jiuniu chat/jiuniu_robot_lsi_class/tests/path\likewei\BigClassDictionary
    :return:
    """
    project_path = os.path.dirname(__file__)
    tests_path = os.path.join(project_path, 'likewei')
    print('tests_path: {}'.format(tests_path))
    tests_2_path = os.path.join(tests_path, 'BigClassDictionary')
    try:
        _lsi = models.LsiModel.load(tests_2_path)
        print('成功加载：{}'.format(_lsi))
    except:
        print('无法加载')
    print(tests_2_path)
    print('type path: {}'.format(type(tests_2_path)))
    tests_3_path = os.path.join(project_path, 'likewei\BigClassDictionary')
    try:
        _lsi = models.LsiModel.load(tests_3_path)
        print('成功加载：{}'.format(_lsi))
    except:
        print('无法加载')
    print(tests_3_path)
test_3()

