#! /user/bin/env python
# -*- coding=utf-8 -*-


import csv


bank_csv_file = csv.reader(open(r'E:\数据挖掘大作业\Project 5 - Bank-additional\bank-additional\bank-additional-full.csv'))

# print(bank_csv_file)

for i in bank_csv_file:
    print(i[0].split(';'))
    # print(i)