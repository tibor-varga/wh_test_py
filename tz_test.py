#!/usr/bin/env python
# Module:   test_tz.py
# Purpose:  convert TZ from UTC to localtime and back
# Date:     N/A
# Notes:
# 1) Ref:  
#    http://stackoverflow.com/questions/4563272/how-to-convert-a-python-utc-datetime-to-a-local-datetime-using-only-python-stand
#

print "tz_test.py:  convert from UTC to localtime and back"

from datetime import datetime
from dateutil import tz

# define timezones here and UTC
HERE = tz.tzlocal()
UTC = tz.gettz('UTC')

# convert time to a datetime structure
TEST_TS='20160606_1201'  # UTC, like that returned by NWS
print "Input string (assumed to be UTC)=", TEST_TS 
dt_u=datetime.strptime(TEST_TS, '%Y%m%d_%H%M')
dt_u=dt_u.replace(tzinfo=UTC)

# convet to a time tuple:
UTC_tmtime=dt_u.timetuple()
dt_h=dt_u.astimezone(HERE)
HERE_tmtime=dt_h.timetuple()

# output the converted times
print "Time UTC =", UTC_tmtime
print "  ", dt_u.ctime()
print "Time HERE=", HERE_tmtime
print "  ", dt_h.ctime()

# convert to printed string
ltime="%04d/%02d/%02d %02d:%02d" %  (dt_h.year, dt_h.month, 
                                     dt_h.day, dt_h.hour, dt_h.minute)
print "Local time=%s" % ltime
ltime=dt_h.strftime('%Y/%m/%d %H:%M')
print "Local time=%s" % ltime
