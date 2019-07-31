#! /user/bin/env python
# -*- coding=utf-8 -*-


import configparser


cf = configparser.ConfigParser()

cf.read("test.conf")
secs = cf.sections()
print(secs)

opts = cf.options("mysql_wind")
print(opts)


kvs = cf.items("mysql_wind")
print(kvs)

db_host = cf.get("mysql_wind", "host")
db_port = cf.getint("mysql_wind", "port")
db_user = cf.get("mysql_wind", "user")
db_pass = cf.get("mysql_wind", "passwd")
db_db = cf.get("mysql_wind", "db")
db_charset = cf.get("mysql_wind", "charset")
print(db_db)
