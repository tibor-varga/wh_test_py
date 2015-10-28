#!/usr/bin/env python
# Module:   py_stringio.py
# Purpose:  Python's string IO
# Date:     N/A
# Notes:
# 1) http://stackoverflow.com/questions/172439/how-do-i-split-a-mult-line-string-into-multiple-lines
# 2) Try with cStringIO first as it is much faster
#

print "py_stringio.py:  StringIO test program"

try:
    print "Trying to use cStringIO first"
    import cStringIO
    StringIO = cStringIO
except ImportError:
    print "cStringIO not found, use StringIO instead"
    import StringIO

my_test="""This is a
test of multiple
lines and more and more
data in multiple lines!
"""

# iterate over lines
ii=1
for line in StringIO.StringIO(my_test):
    line = line.strip()
    print "%03d: %s" % (ii, line)

