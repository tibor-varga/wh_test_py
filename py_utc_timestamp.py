#!/usr/bin/env python
# Module:   py_utc_timestamp.py
# Purpose:  Python UTC timestamp
# Date:     N/A
# Notes:
# 1) ...
# Ref:
#  http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python
#
"""py_utc_timestamp.py:  Python UTC timestamp test"""
from __future__ import division
from datetime import datetime, timedelta
import subprocess

def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 


def py_utc_timestamp():
    """py_utc_timestamp.py:  run the test"""
    print __doc__
    now = datetime.utcnow()
    print now
    print totimestamp(now)

    ref_dt = datetime(2016, 7, 13, 1, 2, 3, 0)
    subprocess.call("date '+%s' -d '2016/7/13 1:2:3 UTC'", shell=True)
    ref_dt_t = 1468371723

    ref_dt_res = totimestamp(ref_dt)
    delta = ref_dt_t - ref_dt_res
    print "ref = {0} t={1} result={2}".format(ref_dt, ref_dt_t, ref_dt_res)
    print "delta={0}".format(delta)

if __name__ == "__main__":
    py_utc_timestamp()
