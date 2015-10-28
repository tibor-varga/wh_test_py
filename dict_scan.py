#!/usr/bin/env python
# Module:   dict_scan.py
# Purpose:  scan dictionary for a word
# Date:     N/A
# Notes:
# 1) Simple I/O and scan program
# 
import sys
import time

DICT="/usr/share/dict/words"
STR='wade'

# open the dictionary
try:
    fd = open(DICT, 'r')
except IOError:
    print "Could not open ", DICT
    sys.exit(1)

# get start time then scan the dictionary
tstart = time.time()

cnt=0
found=0
for line in fd:
    cnt+=1
    if (STR in line):
        ll=line.rstrip()
        print "Cnt=", cnt, " str=", ll
        found+=1

tend = time.time()
tdelta = tend-tstart

print "Total=", cnt, " Found=", found, " DTime=", tdelta, "Sec"
fd.close()

