#!/usr/bin/env python
# Module:   logging_test.py
# Purpose:  test logging to files and console
# Date:     N/A
# Notes:
# 1) https://docs.python.org/3/howto/logging.html
#
import logging as l

LF="mylog.log"
print "logging_test.py:  test of logging to a file w/ time"

# specify format to include time w/ ms, level number and msg
# for other items, see the docs....
l.basicConfig(filename=LF, 
              format='%(asctime)s %(levelname)s %(message)s', 
              level=l.DEBUG)
l.debug('debug msg')
l.info('info msg')
l.warning('warning msg')


print "Created LF w/ data"
f=open(LF,'r')
for line in f:
    line=line.rstrip()
    print line

f.close()
