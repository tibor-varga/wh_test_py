#!/usr/bin/env python
# Module:   toa_1.py
# Purpose:  compute time of arrival events in Python
# Date:     N/A
# Notes:
# 1) Reference:
#  http://preshing.com/20111007/how-to-generate-random-timings-for-a-poisson-process/
#  http://stackoverflow.com/questions/5148635/how-to-simulate-poisson-arrival/18237839#18237839
#  https://docs.python.org/2/library/random.html#random.expovariate
# 2) This uses random.expovariate to create the samples.  These samples
#    are then converted to int.  
# 3) Set the INTERVAL below to the rate.  This is used to create the 
#    rate parameter, lambda = 1/rate.  The resultant mean of samples
#    should be close to this value.  See references for details. 
# 4) Each value is the time of arrival of the next event.  Hence, these values 
#    may be used as input to simulations to simulate discrete events.
#    (Note for real-world systems you may need to add things like minimum event times,
#    guard times, maximum times, etc.)
#

import random

INTERVAL=10
LAMBD=1.0/INTERVAL
SAMPLES=1000
SEED=2

mean = 0
rmean = 0
r = []
s = []


print "toa_1.py:  Time of arrival test "
print "  interval=", INTERVAL
print "  samples=", SAMPLES

# use the same seed each time so we can reproduce results
random.seed(SEED)

# generate the samples and put into an array
for i in range(SAMPLES):
    y = random.expovariate(LAMBD)
    x=int(y)
    r.append(y)
    s.append(x)
    rmean += y
    mean += x
    print "s[%03d]=%d" % (i, x)

# Done, print the mean
print "Done, mean=", mean/SAMPLES, " raw mean=", rmean/SAMPLES
