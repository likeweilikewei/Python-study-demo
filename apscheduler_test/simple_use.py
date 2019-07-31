#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
测试apscheduler
"""

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_study():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '你好')
# scheduler = BlockingScheduler()
# scheduler.add_job(func=aps_test, trigger='cron', second='*/5')
# scheduler.start()


def aps_study2(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
scheduler = BlockingScheduler()
# scheduler.add_job(func=aps_study2, args=('你好呀',), trigger='cron', second='*/5')
job=scheduler.add_job(func=aps_study2, args=('你好呀',), trigger='cron', day_of_week='mon-fri', hour='17', minute='30',second='0')

scheduler.start()
job.remove()
