#!/usr/bin/env python
# Module:   time_datetime.py
# Purpose:  datetime module 
# Date:     N/A
# Notes:
# 1) ...
# Ref:  https://docs.python.org/2/library/datetime.html#module-datetime

import time as t
import datetime as dt

print "time_datetime.py:  get some times and date3s, demonstrate API"
nowt1 = t.time()
print "time_t t1 =     ", nowt1


today=dt.date.today()
print "today date =    ", today

today1=dt.datetime.today()
print "today =         ", today1

#today2=dt.datetime.now('utc')
#print "today(utc) =  ", today2

# expanded method using fromtimestamp and time.time()
today3=dt.datetime.fromtimestamp(t.time())
print "today is also:  ", today3

tb=1000000000
timeb=dt.datetime.fromtimestamp(tb)
print "T=", tb,": ", timeb


d=dt.date(2015,9,1)
t=dt.time(12,13,14)
dc=dt.datetime.combine(d,t)
print "date/time:      ", dc

du=dt.datetime.utcnow()
print "date/time utc:  ", du

# easier:
print "Easier conversion using date/time w/o object"
from datetime import datetime, date, time
d = date(2015, 12, 22)
dn=datetime.now()
print "D=", d
print "DN=", dn

# print custom-formatted time string
print "Custom time string"

# def TZ is UTC, if none supplied assume UTC
tz="UTC"  
if (today3.tzinfo != None):
    tz = today3.tzinfo

# YYYYMMDDTHHMMSS format
tstr="%04d%02d%02dT%02d%02d%02d %s" % \
    (today3.year, today3.month, today3.day, \
     today3.hour, today3.minute, today3.second, tz)
print "TSTR=", tstr
