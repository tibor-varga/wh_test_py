#!/usr/bin/env python
# Module:   make_test_file.py
# Purpose:  make a test file in the test dir
# Date:     N/A
# Notes:
# 1)
#
import time as t
import datetime as dt

TESTDIR="./test"
CNT=10

for i in range(0, CNT):
    now=t.time()
    ds = dt.datetime.fromtimestamp(now)
    tfile="%s/%f.txt" % (TESTDIR, now)
    try:
        tf = open(tfile, "w")
        mystr="%s, %f\n" % (ds, now)
        tf.write(mystr)
        tf.close()
        print "Wrote ", tfile
    except Exception, e:
        print "Exception, e=", e

print "DONE";
