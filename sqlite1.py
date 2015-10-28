#!/usr/bin/env python
# Module:   sqlite1.py
# Purpose:  Sqlite test 1
# Date:     N/A
# Notes:
# 1) Test of Python SQLite interface.
# 2) Define OLD=1 to use sqlite module, not sqlite3
#    (CentOS 5 still only includes the older sqlite module).
# 3) I like to give my SQLITE databases names with a 
#    sqlite suffix (makes it easier when listing dirs).
# 4) Verify on cmd line:
#      sqlite3 test_db.sqlite "select * from test_tbl"
# 5) When done, manually delete the test database, or
#    run the cleanup.py cleanup script....
#
# Ref:  http://zetcode.com/db/sqlitepythontutorial/

# define our test DB
TEST_DB="test_db.sqlite"

print "SQLITE1.PY:  creating and using test db:", TEST_DB

# support older sqlite module for CentOS 5, etc.
OLD=0
if (OLD):
    import sqlite as sl
else:
    import sqlite3 as sl

import sys
from subprocess import call

try:
    # connect/create the test DB then create a cursor
    con = sl.connect(TEST_DB)
    cur = con.cursor()

    # create a test table called "test_tbl" then populate it
    cur.execute('drop table if exists test_tbl')
    cur.execute('create table test_tbl (a int, b text)')
    for i in range (1,11):
        str = "Hello %d" % i
        sql = "insert into test_tbl values(%d, '%s')" % (i, str)
        print "SQL=", sql
        cur.execute(sql)
    # commit the changes, i.e., write to the DBS
    con.commit()

    # from example, get the SQLITE version
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data     
    
except sl.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
# Use "finally:" in Python 2.5 and later (CentOS 5 uses 2.4):
# finally:
    
if con:
    con.close()


