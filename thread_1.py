#!/usr/bin/env python
# Module:   thread_1.py
# Purpose:  thread test program
# Date:     N/A
# Notes:
# 1) Reference:
#     https://docs.python.org/3/library/threading.html
#     https://pymotw.com/2/threading/
#
"""thread test program 1, Timer and Event"""
import threading
from threading import Timer
from threading import Event
import time as t
td = 10.0

# callback function for timer, a sub-class of threads
def hello():
    """callback function for timer, a sub-class of threads"""
    te = t.asctime()
    evt.set()
    print te, ":  hello, world"

# define a worker thread
def my_thread():
    """test worker thread"""
    tt = t.asctime()
    print tt, ":  worker thread running"
    t.sleep(1)
    return

# main below here....
print "thread_1.py:  simple thread test program"

# normal thread test
th = threading.Thread(target=my_thread)

tt = t.asctime()
print tt, ":  thread starting"
th.start()

tt = t.asctime()
print tt, ":  thread joining"
th.join()

tt = t.asctime()
print tt, ":  thread done"
# end of normal thread test...


# event for the timer test
print "create test event and set to F"
evt = Event()

# timer test
print "create a timer for ", td, " seconds"
ts = t.asctime()
tm = Timer(td, hello)
print ts, ":  starting...."
tm.start() # after td seconds, "hello, world" will be printed

tt = t.asctime()
print tt, ":  thread running -- waiting"

evt.wait()
tt = t.asctime()
print tt, ":  got event, exiting"
