#!/usr/bin/env python
# Module:   time_perf.py
# Purpose:  measure time using timeit, time, and clock
# Date:     N/A
# Notes:
#   http://pythoncentral.io/measure-time-in-python-time-time-vs-time-clock/
#   https://docs.python.org/2/library/timeit.html#timeit-examples

TEST_FCN_LOOPS=100
TEST_LOOPS=1000

# dummy test function
import math
def test_fcn():
    y=0
    for x in range(1,TEST_FCN_LOOPS):
        y = y+math.cos(math.pi*x/(TEST_FCN_LOOPS * 1.0))

# function to test using clock() and time()
def test_others():
    print "Testing other timing methods"
    import time
    ts=time.clock()
    for x in range(1, TEST_LOOPS):
        test_fcn()
    dt=time.clock()-ts
    print "time.clock() test=", dt

    ts=time.time()
    for x in range(1, TEST_LOOPS):
        test_fcn()
    dt=time.time()-ts
    print "time.time() test=", dt


# arg passed in setup, see:  timit-examples listed above
# -- use of a main like this is required for the "setup=" item below
if __name__ == '__main__':
    import timeit
    print "time_perf.py:  time profile test"
    print "Test using timeit"
    print(timeit.timeit("test_fcn()", setup="from __main__ import test_fcn", number=TEST_LOOPS))

    test_others()
