#!/usr/bin/env python
# Module:   shelve_test.py
# Purpose:  test of shelve persisting objects 
# Date:     N/A
# Notes:
# 1) Reference:
#      https://docs.python.org/2/library/shelve.html?highlight=shelve
# 2) Notes:
#    - This uses dbm/gdbm/bsddb depending on what is installed.
#    - The shelve module does not support concurrent read/write 
#      access to shelved objects -- NOT THREAD SAFE!
#    - Because the shelve module is backed by pickle, it is insecure 
#      to load a shelf from an untrusted source. 
#  3) Recommend not using shelve/pickle, use JSON instead:
#       http://www.benfrederickson.com/dont-pickle-your-data/
#       -- more portable, non-python-specific, safer, faster....
#
import shelve as s
import random as r

mydb="testdb.sdb"
rcnt=10
print "creating test db",mydb, "with ", rcnt, "records"
db=s.open(mydb, 'c')
for x in range(0,rcnt):
    key="%03d" % x
    val="%10f" % r.random()
    print "K[v]=", key, '[', val, ']'
    db[key]=val

print "using some dict methods"

keys=db.keys()
print "Keys=", keys

ll=len(db)
print "DB size=", ll

print "testing for key 000"
if ('000' in db):
    print "Key 000 found"
else:
    print "key 000 not found"

print "deleting key"
del db['000']
if ('000' in db):
    print "Key 000 found"
else:
    print "key 000 not found"

ll=len(db)
print "DB size=", ll

# -- won't work with JSON w/o additonal code....
cv=1+2j
print "create a complex value",cv,"and add to the shelved data"
db['cv']=cv

# shrink the DB
# not supported by shelve
# db.reorganize()

db.close()

print "opening and looking through all keys"
db=s.open(mydb, 'r')
# use iteritems with anydbm
for k,v in db.iteritems():
    print k, ' ', v

db.close()
