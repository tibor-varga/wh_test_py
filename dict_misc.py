#!/usr/bin/env python
# Module:   dict_misc.py
# Purpose:  misc dictionary functions
# Date:     N/A
# Notes:
# 1) Python tutorial and docs
#    Views:
#      https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
#
import random as r

ITEMS=10
INTERVAL=20
LAMBD=1.0/INTERVAL

print "Create a dictionary of", ITEMS, "items"
td={}
for x in range(0,ITEMS):
    td["x%03d" % x] = "y%04d.00" % r.expovariate(LAMBD)

print "Iterate over the dict items using iteritems()"
for k, v in td.iteritems():
    print k, v

print "Get key view of the dictionary -- these change when dict changes"
tk=td.viewkeys()
print "Len=", len(tk)
for key in tk:
    print "K=", key, "V=", td[key]

print "Adding to dict and then getting all using the view"
td['new'] = "3.14"

print "Len=", len(tk)
for key in tk:
    print "K=", key, "V=", td[key]

print "Deleting new value, getting iterator and using it"
# or del td['new']
del(td['new'])
ti=iter(td)

# add 2 to range so we get the exception"
for x in range(0, len(td)+2):
    try:
        key=ti.next()
        print "K=", key, "V=", td[key]
    except StopIteration:
        print "Iteration done"
        break

print "Use the iterator in a for() loop"
ti=iter(td)
for key in ti:
    print "K=", key, "V=", td[key]

print "Done"
