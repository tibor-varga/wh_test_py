#!/usr/bin/python
# Module:   subproc.py
# Purpose:  subprocess test1 old and new methods
# Date:     N/A
# Notes:    
# 1)  https://docs.python.org/2/library/subprocess.html
#
import os
import subprocess

print "subproc.py:  four ways of running external programs"

# simple os.system call 
#   https://docs.python.org/2/library/os.html#os.system
#   not recommended, docs recommend subprocess
#   may be deprecated 
#   useful for input/output redirection:
#      os.system("some_command < input_file | another_command > output_file")
print "Using os.system, output is to stdout [note: deprecated]"
os.system('ls -l R* L*')
print


# os.popen consuming output, deprecated since v2.6
print "Using os.popen and consuming output [note:  deprecated]"
ios = os.popen('ls -l R* L*', 'r')
for line in ios.readlines():
    print line,
print


print "Using simple subprocess.call w/ shell (shell=True)"
# -- or: 
#       from subprocess import call
#       call(["ls", "-l"])
res = subprocess.call('ls -l R* L*', shell=True)
print

# from examples -- this is the preferred way:
print "Using subprocess.Popen and consuming the output using readlines()"
p = subprocess.Popen('ls -l R* L*', shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print line,
retval = p.wait()
print "  Return value:  ", retval
