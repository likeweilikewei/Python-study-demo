#! /user/bin/env python
# -*- coding=utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

MYSQL_PATH_NEWS = 'mysql+mysqldb://root:123456@127.0.0.1:3306/quant?charset=utf8'
engine = create_engine(MYSQL_PATH_NEWS, echo=True)
Session = sessionmaker(bind=engine)

sql = 'select term from bai_ke_data'
name = pd.read_sql(sql, engine)
f = open('bai_ke', "w", encoding='utf-8')
count = 1
for _, row in name.iterrows():
    count += 1
    if count % 6 == 0:
        f.write("'{}',\n".format(row['term']))
    else:
        f.write("'{}', ".format(row['term']))
f.close()
