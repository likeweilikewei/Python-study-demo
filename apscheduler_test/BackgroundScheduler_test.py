#! /user/bin/env python
# -*- coding=utf-8 -*-

"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BackgroundScheduler()


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour='9-19', second='*/3',max_instances=30)
def tick():
    print('Tick! The time is: %s' % datetime.now())


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour='9-19', second='*/3',max_instances=30)
def li():
    print('li time is :{}'.format(datetime.now()))


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour='9-19', second='*/3',max_instances=30)
def ke():
    print('ke time is :{}'.format(datetime.now()))


@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour='9-19', second='*/3',max_instances=30)
def wei():
    print('wei time is :{}'.format(datetime.now()))



if __name__ == '__main__':
    # scheduler = BackgroundScheduler()
    # scheduler = BlockingScheduler()
    # scheduler.add_job(tick, 'interval', seconds=3)
    # scheduler.add_job(li, 'interval', seconds=3)
    # scheduler.add_job(ke, 'interval', seconds=3)
    # scheduler.add_job(wei, 'interval', seconds=3)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    # scheduler.shutdown()

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        # scheduler.shutdown()
        pass
