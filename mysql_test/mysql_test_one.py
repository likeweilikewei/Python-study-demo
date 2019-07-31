#! /user/bin/env python
# -*- coding=utf-8 -*-

from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# from jiuniu_robot_bayes_class.navice_bayes_of_jiuniu_chat import semantic_recognition


MYSQL_PATH_NEWS = 'mysql+mysqldb://root:123456@127.0.0.1:3306/quant?charset=utf8'
engine = create_engine(MYSQL_PATH_NEWS, echo=True)
Session = sessionmaker(bind=engine)

sql = 'select DISTINCT code, industry from conseption where industry="{}" limit 10'.format('国家队')
# 联合查询
sql_1 = 'select DISTINCT conseption.code, conseption.industry, basic.name from conseption INNER JOIN basic  on (conseption.code=basic.code) where industry="国家队"  limit 10'
session = Session()
sql_result = session.execute(sql).fetchall()
print(sql_result)
