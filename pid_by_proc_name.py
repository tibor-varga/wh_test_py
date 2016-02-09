#!/usr/bin/env python
# Module:   pid_by_proc_name.py
# Purpose:  get pids by process name
# Date:     N/A
# Notes:    
# 1) Read pids by process name from /proc in python using
#    pure python code. This is a program sort-of like the standard
#    Linux pidof program, but in pure Python and directly reading /proc.
#
# 2) Note, this uses "with" hence will NOT work with Python 2.4
#    (for example the native Python on CentOS 5).
#
# 3) ref:  http://stackoverflow.com/questions/3758147/easiest-way-to-read-write-a-files-content-in-python
#    Also see:  http://effbot.org/zone/python-with-statement.htm
#
# 4) Usage:  
#      ./pid_by_proc_name.py bash
#      12470        : bash 
#      12474        : bash 
#      ...etc...

import os
import sys

print "pid_by_proc_name.py:  get PIDs for a proc name, like pidof"

for dirname in os.listdir('/proc'):
    if dirname == 'curproc':
        continue

    try:
        # -- use WITH to open the file, note works only with Python >=2.5
        with open('/proc/{}/cmdline'.format(dirname), mode='rb') as fd:
            # content is array of data read from the file
            content = fd.read().decode().split('\x00')
    except Exception:
        continue

    for i in sys.argv[1:]:
        if i in content[0]:
            print('{0:<12} : {1}'.format(dirname, ' '.join(content)))
