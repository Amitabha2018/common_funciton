#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2020-12-16 17:27'

import time,math,datetime
from datetime import datetime as dt

'''start'''
s = dt.now()
str_s = s.strftime('%Y-%m-%d %H:%M:%S')
tips_sta_en = "Runing start time : "+str_s
tips_sta_ch = "程序开始运行的时间为："+str_s
print(tips_sta_en)

'''function'''
count =0
for i in range(10000000):
    count *= i

'''end'''
e =dt.now()
str_e = e.strftime('%Y-%m-%d %H:%M:%S')
total_second = round((e-s).total_seconds())
tips_end_en = "Runing end time : "+str_e
tips_end_ch = "程序结束运行的时间为："+str_e
print(tips_end_en)

'''runtime'''
run_time = datetime.timedelta(seconds=total_second)
total_run_time_en ="Runing total time: " + str(run_time)
total_run_time_ch ="程序运行总时间为: " + str(run_time)
print(total_run_time_en)

