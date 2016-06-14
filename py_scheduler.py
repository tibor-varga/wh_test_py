#!/usr/bin/env python
# Module:   py_scheduler.py
# Purpose:  Python scheduler test
# Date:     N/A
# Notes:
# 1) See https://docs.python.org/2.7/library/sched.html
# 2) See notes about issues with threads....
# 3) This is similar to the linked list timer Q I used
#    in some test code (glib2-based).
# 4) This is not recommended, recommended to use Timer
#
"""Schedulder example, recommended is to use Timer instead"""

# Defines:
num = 10  # number of events
tmo = 2   # sec timeout

import sched, time

# create a new scheduler using real-time:
#   time_func is time.time
#   delay_func is time.sleep
# -- these can be changed, e.g., for "simulated" time
SCH = sched.scheduler(time.time, time.sleep)

# event handler (callback)
def print_time():
    """Print current time"""
    print "From print_time: ", time.time()

# function to run the test
def print_some_times():
    """Print times used by the schedule"""
    print "From main:       ", time.time()
    SCH.enter(5, 1, print_time, ())
    SCH.enter(10, 1, print_time, ())
    # start it and run the events....
    SCH.run()
    print "From main:       ", time.time()

def pt_2():
    """print times and reschedule"""
    print_time()
    global num
    num = num - 1
    if num > 0:
        SCH.enter(tmo, 1, pt_2, ())

# do the test
print_some_times()

# test of a periodic schedule
print "Periodic test, num=%d, tmo=%d sec" % (num, tmo)

#SCH_enter(tmo, 1, pt_2, ())
pt_2()
SCH.run()

print "Done!"

