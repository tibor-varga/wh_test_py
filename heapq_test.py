#!/usr/bin/env python
# Module:   heapq_test.py
# Purpose:  test heapq module
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/heapq.html
#
import heapq
import time as t
import random as r
DICT="/usr/share/dict/words"

print "heapq_test.py:  test heapq on random data"

# use the below values for some really large data sets
# CNT=1000000
# verbose=0
CNT=10
verbose=1
h=[]

print "opening dict ", DICT
try:
    fd = open(DICT, 'r')
except IOError:
    print "Could not open ", DICT
    sys.exit(1)

print "adding tuples of a random key and a dict word"
tts=t.time()
dtsum=0
for x in range(0, CNT):
    ts=t.time()
    val=r.random()
    de=fd.readline()
    de=de.rstrip()
    if verbose > 0:
        print "Push(%010f, %s)" % (val, de)
    heapq.heappush(h, (val, de))
    dt=t.time()-ts
    dtsum=dtsum+dt

dtt=t.time()-tts
dtavg=dtsum/CNT
print "Total time=", dtt
print "Average time=", dtavg

print "Removing from the queue, output is sorted"
tts=t.time()
for x in range(len(h)):
    ts=t.time()
    x,y = heapq.heappop(h)
    if verbose>0:
        print "Pop()->%10f,%s" % (x,y)
    dt=t.time()-ts
    dtsum=dtsum+dt

dtt=t.time()-tts
dtavg=dtsum/CNT
print "Total time=", dtt
print "Average time=", dtavg

print "Done"
