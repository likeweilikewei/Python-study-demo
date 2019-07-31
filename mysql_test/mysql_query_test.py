#! /user/bin/env python
# -*- coding=utf-8 -*-


import time
import pymysql
import pandas as pd
from flask import request
from contextlib import contextmanager
from flask import Blueprint
from quant_backend.settings.settings import ENV,aliyun_engine

paper_api = Blueprint('paper_api',__name__)

config_production = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'quant_start',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

config_development = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'db': 'quant_new',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

if ENV == 'production':
    config = config_production
else:
    config = config_development

connection = pymysql.connect(**config)
connection.autocommit(True)


# 定义回滚和关闭操作
@contextmanager
def cursors():
    cursor_tmp = connection.cursor()
    try:
        yield cursor_tmp
        # 设置了自动提交不需要手动提交
        # connection.commit()
    except Exception as e:
        connection.rollback()
        print('sql operation error:{}'.format(e))
        raise Exception('sql operation error:{}'.format(e))
    finally:
        cursor_tmp.close()


class SqlTest:
    """
    选股部分速度测试
    """
    @staticmethod
    def sql_test(sql,sql_message,sql_new=None):
        """
        测试sql语句的查询速度
        :param sql
        :param sql_message:
        :param sql_new:优化后的sql
        :return:
        """
        time1 = time.time()
        with cursors() as __cursor:
            __cursor.execute(sql)
            cursor_result = __cursor.fetchall()
            # print(cursor_result)
            if cursor_result:
                cursor_result = pd.DataFrame(cursor_result)
            # print('pymysql result:{}'.format(cursor_result))
        time2 = time.time()
        df = pd.read_sql('select code from basic', aliyun_engine)
        # print('orm result:{}'.format(df))
        time3 = time.time()
        if not sql_new:
            print('{},\nsql:{},\npymysql cost:{} s, {} ms\norm cost:{} s, {} ms\npymysql的速度是orm的 {} 倍\n'.format(sql_message, sql,round(time2 - time1,4),round((time2-time1)*1000,2),round(time3 - time2,4),round((time3-time2)*1000,2), round((time3-time2)/(time2-time1),2)))
        else:
            time4 = time.time()
            with cursors() as __cursor:
                __cursor.execute(sql_new)
                cursor_result = __cursor.fetchall()
                cursor_result = pd.DataFrame(cursor_result)
                print('pymysql new sql result:{}'.format(cursor_result))
            time5 = time.time()
            print('{},\nsql:{},\npymysql cost:{} s, {} ms\norm cost:{} s, {} ms\npymysql的速度是orm的 {} 倍'.format(sql_message, sql,round(time2 - time1,4),round((time2-time1)*1000,2),round(time3 - time2,4),round((time3-time2)*1000,2), round((time3-time2)/(time2-time1),2)))
            print('new sql:{},\npymysql new cost{} s, {} ms\n优化后的pymysql速度是旧语句的 {} 倍\n'.format(sql_new,round(time5 - time4,4),round((time5-time4)*1000,2),round((time3-time2)/(time5-time4),2)))

    def find_stock_codes(self):
        """
        得到股票
        :return:
        """
        __sql = 'select code from basic'
        self.sql_test(sql=__sql,sql_message='得到股票')

    def find_st(self):
        """
        获取st
        :return:
        """
        __sql = 'select code, entry_dt, remove_dt from st'
        self.sql_test(sql=__sql,sql_message='获取st')

    def mysql_test(self):
        """
        总的入口函数
        :return:
        """
        self.find_stock_codes()
        self.find_st()
        self.find_second_new()
        self.find_regionals_code()
        self.find_margin_code()
        self.find_conseption()
        self.find_index_code()
        self.find_industry_code()
        self.find_all_code()
        self.find_ah_connection()
        self.benchmark_history_1()
        self.benchmark_history_2()
        self.suspendeds()
        self.valuation()
        self.technical()
        self.calender()

    def find_second_new(self):
        """
        获取次新股票
        :return:
        """
        __sql = 'select code,list_date,delist_date from basic'
        self.sql_test(sql=__sql,sql_message='获取次新股票')

    def find_regionals_code(self):
        """
        获取地域股票
        :return:
        """
        __sql = 'select code, region from regionals'
        self.sql_test(sql=__sql,sql_message='获取地域股票')

    def find_margin_code(self):
        """
        筛选融资融券股票
        :return:
        """
        date = '2010-03-31'
        __sql = 'select code, date from margintrade WHERE date = "{}"'.format(date)
        self.sql_test(sql=__sql,sql_message='筛选融资融券股票')

    def find_conseption(self):
        """
        筛选股票股票，时间+行业
        :return:
        """
        __sql = 'select gn_code as category, code, list_date, delist_date from conseption'
        self.sql_test(sql=__sql,sql_message='筛选股票股票，时间+行业')

    def find_index_code(self):
        """
        获取指数成份股,可能为in数据
        :return:
        """
        __sql = 'select code, category, list_date, delist_date from indexs'
        self.sql_test(sql=__sql,sql_message='获取指数成份股,可能为in数据')

    def find_industry_code(self):
        """
        获取行业成份股
        :return:
        """
        __sql = 'select code, industry_code, hy_code, start_date, end_date from industry'
        self.sql_test(sql=__sql,sql_message='获取行业成份股')

    def find_all_code(self):
        """
        获取所有股票
        :return:
        """
        __sql = 'select code,list_date,delist_date from basic'
        self.sql_test(sql=__sql,sql_message='获取所有股票')

    def find_ah_connection(self):
        """
        find_ah_connection
        :return:
        """
        __sql = 'select sse_code from hh_stock_connection'
        self.sql_test(sql=__sql,sql_message='find_ah_connection')

    def benchmark_history_1(self):
        """
        获得历史基准数据
        :return:
        """
        __sql = "select code, date, befor_day, niubear, ups, open, close from timing as t where code='{}' ORDER BY date DESC limit 1".format(
                    '399905.SZ')
        self.sql_test(sql=__sql,sql_message='获得历史基准数据')

    def benchmark_history_2(self):
        """
        获得历史基准数据2
        :return:
        """
        __sql = "select code, date, befor_day, niubear, ups, open, close from timing where code='{}' and date>='{}' and date<='{}' order by date".format(
            '399905.SZ',
                    '2010-09-17',
                    '2017-09-17')
        self.sql_test(sql=__sql,sql_message='获得历史基准数据')

    def suspendeds(self):
        """
        获取停牌股
        :return:
        """
        __sql="""SELECT code FROM suspended WHERE list_date = '{}'
        	        """.format('2002-09-03')
        self.sql_test(sql=__sql,sql_message='获取停牌股')

    def valuation(self):
        """
        获取基本面指标
        :return:
        """
        __sql = """SELECT * FROM valuation_{} WHERE date = '{}'""".format('2018', '2018-11-01')
        self.sql_test(sql=__sql,sql_message='获取基本面指标')
    
    def technical(self):
        """
        获取技术指标
        :return:
        """
        __sql = """SELECT * FROM technical_{} WHERE date = '{}'""".format('2018', '2018-11-01')
        self.sql_test(sql=__sql,sql_message='获取技术指标')

    def calender(self):
        """
        日历查找
        :return:
        """
        __sql = """select trade_days from calendar where trade_days > '{}' and trade_days<= '{}'
			""".format('2013-12-21', '2018-07-09')
        self.sql_test(sql=__sql,sql_message='日历查找')

sql_test = SqlTest()
sql_test.mysql_test()
