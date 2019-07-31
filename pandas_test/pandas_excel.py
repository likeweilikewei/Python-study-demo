#! /user/bin/env python
# -*- coding=utf-8 -*-

import datetime
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

MYSQL_PATH = 'mysql+mysqldb://root:123456@127.0.0.1:3306/quant_new?charset=utf8&local_infile=1'
engine = create_engine(MYSQL_PATH, echo=True)

MYSQL_PATH_WIND = 'mysql+mysqldb://root:123456@127.0.0.1:3306/wind?charset=utf8'  # new
engine_wind = create_engine(MYSQL_PATH_WIND, echo=True)

data=pd.read_excel(r'D:\文档\霞妹\十二大军工集团上市企业-威宝备注.xlsx',sheet_name='Sheet1')
data=data.fillna(method='ffill')
data=data.drop(columns=['股票代码','上市日期','行业名称','备注'])
names=tuple(data['股票名'])
print(names)
print(data)
print('\n')

# planInfo = pd.read_sql_query(
#     sql='SELECT SUBSTRING(ashareindustriesclass.WIND_CODE,1,6),ashareindustriescode.INDUSTRIESNAME FROM ashareindustriesclass LEFT JOIN ashareindustriescode ON ashareindustriesclass.WIND_IND_CODE=ashareindustriescode.INDUSTRIESCODE'
#     , con=engine_wind)
# planInfo = planInfo.rename(columns={
#     'SUBSTRING(ashareindustriesclass.WIND_CODE,1,6)': '股票代码',
#     'INDUSTRIESNAME': '行业名称',
# })
# print(planInfo)

planInfo=pd.read_sql(sql='SELECT SUBSTRING(code,1,6),industry,start_date,end_date from industry',con=engine)
planInfo = planInfo.rename(columns={
    'SUBSTRING(code,1,6)': '股票代码',
    'industry': '行业名称',
    'start_date':'行业进入时间',
    'end_date':'行业退出时间'
})
# planInfo=planInfo.replace({'股票代码':'000001'},'sss')
planInfo=planInfo.replace({'行业退出时间':datetime.datetime.strptime('9999-01-01','%Y-%m-%d').date()},np.nan)
planInfo[['行业进入时间','行业退出时间']]=planInfo[['行业进入时间','行业退出时间']].astype(str)
planInfo=planInfo.replace({'行业退出时间':'nan'},np.nan)
print(planInfo)

code_name_small=pd.read_sql(sql='SELECT S_INFO_CODE,S_INFO_NAME,S_INFO_LISTDATE,S_INFO_DELISTDATE FROM asharedescription',con=engine_wind)
code_name_small = code_name_small.rename(columns={
    'S_INFO_CODE': '股票代码',
    'S_INFO_NAME': '股票名',
    'S_INFO_LISTDATE':'上市日期',
'S_INFO_DELISTDATE':'退市日期'})

data_industry=pd.merge(data,code_name_small,how='left',on='股票名')
data_industry=pd.merge(data_industry,planInfo,how='left',on='股票代码')
print(data_industry)
data_industry.to_excel(r'D:\文档\霞妹\十二大军工集团上市企业-行业信息-威宝整理版.xlsx')

# print(planInfo['行业进入时间'].values[0])
# print(type(planInfo['行业进入时间'].values[0]))
codes=pd.read_sql(sql='SELECT S_INFO_WINDCODE FROM asharedescription WHERE S_INFO_NAME in {}'.format(names),con=engine_wind)
# print('codes:{}'.format(codes))
codes=tuple(codes['S_INFO_WINDCODE'])
print(codes)

# code_name=pd.read_sql(sql='SELECT asharedescription.S_INFO_CODE,asharedescription.S_INFO_NAME,asharedescription.S_INFO_LISTDATE,\
# asharesalessegment.REPORT_PERIOD,asharesalessegment.S_SEGMENT_ITEM,asharesalessegment.S_SEGMENT_SALES,asharesalessegment.S_SEGMENT_PROFIT,asharesalessegment.S_SEGMENT_COST,\
# asharesalessegment.PCT_SEGMENT_SALES,asharesalessegment.PCT_SEGMENT_PROFIT,asharesalessegment.PCT_SEGMENT_COST,\
# asharesalessegment.INC_SEGMENT_SALES,asharesalessegment.INC_SEGMENT_PROFIT,asharesalessegment.INC_SEGMENT_COST,\
# asharesalessegment.GROSS_PROFIT_MARGIN,asharesalessegment.INC_PROFIT_MARGIN FROM asharedescription LEFT JOIN asharesalessegment ON asharedescription.S_INFO_WINDCODE=asharesalessegment.S_INFO_WINDCODE WHERE asharedescription.S_INFO_WINDCODE IN {}'.format(codes),con=engine_wind)
# code_name = code_name.rename(columns={
#     'S_INFO_CODE': '股票代码',
#     'S_INFO_NAME': '股票名',
#     'S_INFO_LISTDATE':'上市日期',
#
#     'REPORT_PERIOD': '报告日期',
#     'S_SEGMENT_ITEM': '主营业务项目',
#     'S_SEGMENT_SALES': '主营业务收入(元)',
#     'S_SEGMENT_PROFIT': '主营业务利润(元)',
#     'S_SEGMENT_COST': '主营业务成本(元)',
#     'PCT_SEGMENT_SALES': '主营业务收入占比(%)',
#     'PCT_SEGMENT_PROFIT': '主营业务利润占比(%)',
#     'PCT_SEGMENT_COST': '主营业务成本占比(%)',
#     'INC_SEGMENT_SALES': '主营业务收入同比增长率(%)',
#     'INC_SEGMENT_PROFIT': '主营业务利润同比增长率(%)',
#     'INC_SEGMENT_COST': '主营业务成本同比增长率(%)',
#     'GROSS_PROFIT_MARGIN': '毛利率(%)',
#     'INC_PROFIT_MARGIN': '毛利率增长率(%)',
# })

code_name=pd.read_sql(sql='SELECT asharedescription.S_INFO_CODE,asharedescription.S_INFO_NAME,\
asharesalessegment.REPORT_PERIOD,asharesalessegment.S_SEGMENT_ITEM,asharesalessegment.S_SEGMENT_SALES,asharesalessegment.S_SEGMENT_PROFIT,asharesalessegment.S_SEGMENT_COST,\
asharesalessegment.PCT_SEGMENT_SALES,asharesalessegment.PCT_SEGMENT_PROFIT,asharesalessegment.PCT_SEGMENT_COST,\
asharesalessegment.INC_SEGMENT_SALES,asharesalessegment.INC_SEGMENT_PROFIT,asharesalessegment.INC_SEGMENT_COST,\
asharesalessegment.GROSS_PROFIT_MARGIN,asharesalessegment.INC_PROFIT_MARGIN FROM asharedescription LEFT JOIN asharesalessegment ON asharedescription.S_INFO_WINDCODE=asharesalessegment.S_INFO_WINDCODE WHERE asharedescription.S_INFO_WINDCODE IN {}'.format(codes),con=engine_wind)
code_name = code_name.rename(columns={
    'S_INFO_CODE': '股票代码',
    'S_INFO_NAME': '股票名',
    'S_INFO_LISTDATE':'上市日期',

    'REPORT_PERIOD': '报告日期',
    'S_SEGMENT_ITEM': '主营业务项目',
    'S_SEGMENT_SALES': '主营业务收入(元)',
    'S_SEGMENT_PROFIT': '主营业务利润(元)',
    'S_SEGMENT_COST': '主营业务成本(元)',
    'PCT_SEGMENT_SALES': '主营业务收入占比(%)',
    'PCT_SEGMENT_PROFIT': '主营业务利润占比(%)',
    'PCT_SEGMENT_COST': '主营业务成本占比(%)',
    'INC_SEGMENT_SALES': '主营业务收入同比增长率(%)',
    'INC_SEGMENT_PROFIT': '主营业务利润同比增长率(%)',
    'INC_SEGMENT_COST': '主营业务成本同比增长率(%)',
    'GROSS_PROFIT_MARGIN': '毛利率(%)',
    'INC_PROFIT_MARGIN': '毛利率增长率(%)',
})
code_name=code_name.sort_values(by=['股票代码','报告日期','主营业务项目'],ascending=[True,True,True])

code_name.reset_index(drop=True, inplace=True)
print(code_name)
code_name.to_excel(r'D:\文档\霞妹\十二大军工集团上市企业-主营业务-威宝整理版.xlsx')


