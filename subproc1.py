#!/usr/bin/python
# Module:   subproc1.py
# Purpose:  subprocess tests, expanded
# Date:     N/A
# Notes:    
# 1)  https://docs.python.org/2/library/subprocess.html
#
import subprocess
import os

print "subproc1.py:  more ways of running external pgms and consuming data"

print "Using simple subprocess.call w/o shell)"
#       from subprocess import call
#       call(["ls", "-l"])
print "  This will fail as no shell to expand R*:  ['ls', '-l', 'R*', 'L*']"
res = subprocess.call(['ls', '-l', 'R*', 'L*'])
print "  THis will work:  ['ls', '-l', 'README.md', 'LICENSE']"
res = subprocess.call(['ls', '-l', 'README.md', 'LICENSE'])
print

# from examples -- this is the preferred way:
print "Using subprocess.Popen and consuming the output using readlines()"
p = subprocess.Popen(['ls', '-l', 'README.md', 'LICENSE'], 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
print "  Return value:  ", retval

# test with exception
print "Using exception to try program lsxx which does not exist"
try:
    res = subprocess.call(['lsxx', '-l', 'R*', 'L*'])
    print
except Exception, e:
    print "Exception , e=", e

# test with redirection
print "Using call w/ redirection and exception w/ else"

# do the ls -l with redirection to F
F="lsl.dat"
CMD="ls -l >"+F
try:
    os.system(CMD)
except: 
    print "System error"
else: 
    print "Ran ", CMD

cnt=0
try:
    f = open(F)
    for line in f:
        # print line,
        cnt=cnt+1
    f.close()
    #print "Count=",cnt
except:
    print "Exception File error"
else:
     print "No exception, Count=",cnt

print "Done!"

