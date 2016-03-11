#!/usr/bin/env python
# Module:   regex_test.py
# Purpose:  test Python regex
# Date:     N/A
# Notes:
# 1) https://docs.python.org/3/library/re.html
#    http://www.tutorialspoint.com/python/python_reg_expressions.htm

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

print "Example from tutorialspoint:"
line = "Cats are smarter than dogs"
print "Testing line=\"%s\"" % line
print "RE is a raw string matching multiple tokens\n"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group()  : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

print "Done"
        
