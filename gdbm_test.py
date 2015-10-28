#!/usr/bin/env python
# Module:   gdbm_test.py
# Purpose:  gdbm test 
# Date:     N/A
# Notes:
# 1) Reference:
#      https://docs.python.org/2/library/gdbm.html
#
import gdbm
import random as r

mydb="testdb.gdbm"
rcnt=10
print "creating test db",mydb, "with ", rcnt, "records"
db=gdbm.open(mydb, 'c')
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

# shrink the DB
db.reorganize()


db.close()

print "opening and looking through all keys"
db=gdbm.open(mydb, 'r')
# use iteritems with anydbm
#for k,v in db.iteritems():
k=db.firstkey()
while k != None:
    v=db[k]
    print k, ' ', v
    k = db.nextkey(k)

db.close()


