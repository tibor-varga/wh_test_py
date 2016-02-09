#!/usr/bin/env python
# Module:   py_with.py
# Purpose:  open a file and consume it using with
# Date:     N/A
# Notes:
# 1) First create a test file then read using "with"
# 2) This will only work with Python 2.5 or later (hence
#    it will NOT work with the Python 2.4 on CentOS 5).
#
import time as t
import datetime as dt

tname="py_with"

CNT=10

print "py_with:  create test file then read using \"with\""

now=t.time()
ds = dt.datetime.fromtimestamp(now)
tfile="%f.txt" % (now)
print "Creating %s" % tfile
try:
    tf = open(tfile, "w")
    mystr="%s, %f\n" % (ds, now)
    tf.write(mystr)
    tf.close()
    print "Wrote ", tfile
except Exception, e:
    print "Exception, e=", e

print ""
print "Reading file back using \"with\""
try:
    with open(tfile) as f:
        data = f.read()
        print "Read data as:  %s" % data
except Exception, e:
    print "Exception, e=", e
    

print "DONE";
