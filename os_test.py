#!/usr/bin/env python
# Module:   os_test.py
# Purpose:  test/demo the OS module
# Date:     N/A
# Notes:  
# 1) https://docs.python.org/2/library/os.html
#
import os

OS_NAME=os.name
OS_UNAME=os.uname()
print "OS Name=", OS_NAME, OS_UNAME

HOME=os.environ['HOME']
print "Home=", HOME

CWD=os.getcwd()
print "Current Dir=", CWD

UID=os.getuid()
GID=os.getgid()
USER=os.getlogin()
print "User=", USER, "GID:UID", GID, ":", UID

print "Creating a temp file and reading/writing it"
tfile=os.tmpfile()
tfile.write("Hello 1\n")
tfile.write("Hello 2\n")
tfile.seek(0)
for x in tfile:
    x=x.rstrip()
    print x

tfd=tfile.fileno()
tstat=os.fstat(tfd)
print "Stat info on temp file=", tstat
vfsinfo=os.fstatvfs(tfd)
print "VFS info on temp file=", vfsinfo

print "truncating file, then writing new data"
os.ftruncate(tfd,0)
tfile.write("Hello a\n")
tfile.write("Hello b\n")
tfile.seek(0)
for x in tfile:
    x=x.rstrip()
    print x

tfile.close();

print "Getting list of files in this dir"
# note, list is not sorted so we sort it here
dl=os.listdir(".")
dl.sort()
ii=1
for x in dl:
    print "%03d:  %s" % (ii,x)
    ii=ii+1


print "forking a child and waiting for it to return"

cpid=os.fork()
if (cpid == 0):
    CMD="python -c \"import os; print os.times()\""
    print "Child, running cmd=", CMD
    os.system(CMD)
    import sys
    sys.exit(2)

print "Parent, waiting on child=", cpid
pid, estatus = os.waitpid(cpid, 0)
sig=estatus&0xFF
val=(estatus&0xFF00) >> 8
print "Child exited, status,sig,val=", estatus, sig, val
