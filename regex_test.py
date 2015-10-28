#!/usr/bin/env python
# Module:   regex_test.py
# Purpose:  test Python regex
# Date:     N/A
# Notes:
# 1) https://docs.python.org/3/library/re.html
#

import re
import sys

DICT="/usr/share/dict/words"
CNT=100

print "regex_text.py:  simple regex test for strings starting w/ X|Y"

myre=re.compile('^X|^Y')

# open the dictionary
try:
    fd = open(DICT, 'r')
except IOError:
    print "Could not open ", DICT
    sys.exit(1)

for line in fd:
    m = myre.match(line)
    if m:
        print m.string.rstrip()

# Note, if the string ends with a period or similar re.split will
# return an empty stirng at the end.  If it starts with a non-word,
# the result will start with an empty string as well....
tstr="This is a very long string  with some-extra stuff in   it."
print "Using re.split('\W+',s) to split \"", tstr, "\""
parts=re.split('\W+', tstr)
ii=1
for x in parts:
    print "%03d:  %s" % (ii,x)
    ii=ii+1

print "Using the normal str.split() function"
parts=tstr.split()
ii=1
for x in parts:
    print "%03d:  %s" % (ii,x)
    ii=ii+1

print "Done"
        
