#!/usr/bin/env python
# Module:   queue.py
# Purpose:  implement a queue
# Date:     N/A
# Notes:
# 1) tbd
# Ref:  
#   https://docs.python.org/2/tutorial/datastructures.html
#
from collections import deque

print "QUEUE:  create a queue and add elements"
q = deque()
for ii in range(0,100):
    s="Item-%03d" % (ii)
    q.append(s)

# add one more to the left
q.appendleft('Left append')

#print q

# get and display length
cnt = len(q)
print "Item count=", cnt

# pop first 5 elements
for ii in range(0,5):
    x=q.popleft()
    print "Item %03d = %s" % (ii, x)

# reverse then pop 5 more
print "Reversing elements"
q.reverse()
for ii in range(0,5):
    x=q.popleft()
    print "Item %03d = %s" % (ii, x)

# clear it
q.clear()

# get and display length
cnt = len(q)
print "Item count after clear=", cnt

