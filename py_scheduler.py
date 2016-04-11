#!/usr/bin/env python
# Module:   py_scheduler.py
# Purpose:  Python scheduler test
# Date:     N/A
# Notes:
# 1) See https://docs.python.org/2.7/library/sched.html
# 2) See notes about issues with threads....
# 3) This is similar to the linked list timer Q I used
#    in some test code (glib2-based).
#
import sched, time

# create a new scheduler using real-time:
#   time_func is time.time
#   delay_func is time.sleep
# -- these can be changed, e.g., for "simulated" time
s = sched.scheduler(time.time, time.sleep)

# event handler (callback)
def print_time(): print "From print_time: ", time.time()

# function to run the test 
def print_some_times():
    print "From main:       ", time.time()
    s.enter(5, 1, print_time, ())
    s.enter(10, 1, print_time, ())
    # start it and run the events....
    s.run()
    print "From main:       ", time.time()
    
# do the test
print_some_times()
print "Done!"
