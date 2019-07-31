#! /user/bin/env python
# -*- coding=utf-8 -*-

from airflow.operators import BashOperator, DummyOperator
from airflow.models import DAG
from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                  datetime.min.time())
args = {
    'owner': 'airflow',
    'start_date': seven_days_ago,
}

dag = DAG(
    dag_id='dag2',
    default_args=args,
    schedule_interval="30 17 * * *"  # 这里可以填crontab时间格式
    )

task0 = DummyOperator(task_id='task0', dag=dag)

cmd = 'ls -l'
task1 = BashOperator(
    task_id = 'task1',
    bash_command = cmd,
    dag = dag)

task0.set_downstream(task1)

task2 = DummyOperator(
        trigger_rule = 'all_done',
        task_id =  'task2',
        dag = dag,
        depends_on_past = True)

task2.set_upstream(task1)

task3  = DummyOperator(
        trigger_rule = 'all_done',
        depends_on_past = True,
        task_id = 'task3',
        dag = dag)

task3.set_upstream(task2)

task4 = BashOperator(
    task_id = 'task4',
    bash_command = 'lsfds-ljss',
    dag = dag)

task5 = DummyOperator(
        trigger_rule = 'all_done',
        task_id = 'task5',
        dag = dag)

task5.set_upstream(task4)
task5.set_upstream(task3)
