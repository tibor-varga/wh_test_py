#!/usr/bin/env python
# Module:   syslog_test.py
# Purpose:  test syslog using syslog module and syslog handler
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/syslog.html
#    https://docs.python.org/2/library/logging.handlers.html
# 2) Notes about older Python 2.4 as used by CentOS 5.
#

PNAME="syslog_test"
print "syslog_test.py:  syslog using syslog module and syslog handler"

# use syslog module -- much, much simpler
print "Using syslog module to send Info, Notice, Warning"
import syslog
FAC=syslog.LOG_LOCAL1

# for CentOS 5, no keyword args, just pass parms:
#   syslog.openlog(['ident string'[, logoption [, facility]]])
#   syslog.logopen('mypgm', syslog.LOG_PID|syslog.LOG_CONS, syslog.LOG_LOCAL1)
#
syslog.openlog(logoption=syslog.LOG_PID|syslog.LOG_CONS, facility=FAC)
syslog.syslog(syslog.LOG_INFO, "Info msg via syslog")
syslog.syslog(syslog.LOG_NOTICE, "Notice msg via syslog")
syslog.syslog(syslog.LOG_WARNING, "Warning msg via syslog")

syslog.closelog()

# use a log handler -- great if you want multiple handlers
# or want to use web server logging or some other type as well....
print "Using logging module w/ syslog handler for multiple msgs"
import logging
import logging.handlers
from logging.handlers import SysLogHandler

l=logging.getLogger('MyLogger')
l.setLevel(logging.INFO)  # no logging.NOTICE
lh=SysLogHandler(address='/dev/log', facility=SysLogHandler.LOG_LOCAL1)
l.addHandler(lh)

l.info('SLH:  info msg')
l.warning('SLH:  warning msg')
l.debug('SLH:  debug msg')
l.critical('SLH:  critical msg')

l.info('Done')
lh.close()






