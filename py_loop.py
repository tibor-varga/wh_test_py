#!/usr/bin/env python
# Module:   py_loop.py
# Purpose:  loop and do work -- used for debugger tests
# Date:     N/A
# Notes:

import time as t
import os
import sys
import math

#-------------------------------------------------------------------
# work func
def work_func(ii):
    x=math.cos(ii*math.pi)
    print "ii=%d x=%f" % (ii, x)

#-------------------------------------------------------------------
class tclass:
    def __init__(self, a):
        self.a = a
    def empty(self):
        self.a = None
    def work(self, i):
        work_func(i)

#-------------------------------------------------------------------
def sub_func():
    x=tclass('b')
    for i in range (0,1000):
        x.work(i)
        t.sleep(1)

#-------------------------------------------------------------------
# main function

print "py_loop:  Loop and do stuff for debugger"
my_pid=os.getpid()

sub_func()

print "Done"



