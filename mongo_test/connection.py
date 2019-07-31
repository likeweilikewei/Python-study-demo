#! /user/bin/env python
# -*- coding=utf-8 -*-

from pymongo import MongoClient
from pymongo import Connection
import time

# 库名
db = MongoClient('mongodb://127.0.0.1:3717,127.0.0.1:3717/admin?replicaSet=mgset-123456')
db.admin.authenticate('root', '123456')
