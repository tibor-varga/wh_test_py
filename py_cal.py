#!/usr/bin/env python
# Module:   py_cal.py
# Purpose:  calendar test 
# Date:     N/A
# Notes:
# 1) 
# Ref:  any references
#
import calendar
calendar.setfirstweekday(calendar.SUNDAY)

yr=2015

mycal = calendar.calendar(yr)
print "Mycal=", mycal

print "Is leap=", calendar.isleap(yr)

dow=calendar.weekday(yr,10,31)
print "Halloween is on:  ", dow
