#!/usr/bin/env python
# Module:   time_fcn.py
# Purpose:  test time functions
# Date:     N/A
# Notes:
# 1) This uses the time functions based on C libs and functions.
#    For more features and OOP it is recommended to use datetime.

print "time_fcn.py:  time tests, UNIX time functions based on C lib"
import time as t

mt=t.time()
print "UNIX time now=", mt

tg=t.gmtime()
tl=t.localtime()
ta=t.asctime()
print "  asctime=", ta
print "  gmtime, localtime='\n  ", tg, '\n  ', tl

print "Year is:  ", tl.tm_year

# test Y2K 
ttest=(2000,12,31,23,59,59,0,0,0)
tm=t.mktime(ttest)
print "Y2K-1s=", ttest,' tm=', tm

# make some time strings
ltime="%04d/%02d/%02d %02d:%02d" % (tl.tm_year, tl.tm_mon, tl.tm_mday, 
                                 tl.tm_hour, tl.tm_min)

st=t.strftime("%Y/%m/%d %H:%M %Z", tl)
print("Local time=%s or from strftime=%s") % (ltime, st)

import math as m
MR=100000
yy=0

print "timing test -- use t.clock() to time Python"
ts=t.clock()
for x in range(0,MR):
    dx=x/(2*m.pi)
    y=m.cos(dx)
    yy+=y

dt=t.clock()-ts
print "Elapsed=", dt

print "convert string to time struct, add 1 month"
st = t.strptime("20150501", "%Y%m%d")
print "T=", st

for x in range(0, 12):
    stw = list(st)
    stw[1]=(stw[1])%12 + 1  # sub 1 to make 0..12, add 1, modulo, add 1
    st=t.struct_time(tuple(stw))
    print x, st


    

