#!/usr/bin/env python3
# Module:   py_utc_timestamp_p3.py
# Purpose:  UTC timestamp on Python 3 -- very simple
# Date:     N/A
# Notes:
# 1) ...
# Ref:  any references
#  http://stackoverflow.com/questions/8777753/converting-datetime-date-to-utc-timestamp-in-python
"""py_utc_timestamp_p3.py:  Python UTC timestamp in python 3"""

from __future__ import division
from datetime import datetime, timedelta, timezone
import subprocess

def py_utc_timestamp_p3():
    __doc__
    print(__doc__)
    ref_dt = datetime(2016, 7, 13, 1, 2, 3, 0)
    subprocess.call("date '+%s' -d '2016/7/13 1:2:3 UTC'", shell=True)
    ref_dt_t = 1468371723
    ref_dt_res = ref_dt.replace(tzinfo=timezone.utc).timestamp()
    delta = ref_dt_t - ref_dt_res
    print("ref = {0} t={1} result={2}".format(ref_dt, ref_dt_t, ref_dt_res))
    print("delta={0}".format(delta))


if __name__ == "__main__":
    py_utc_timestamp_p3()
