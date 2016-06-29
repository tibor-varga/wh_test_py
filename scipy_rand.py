#!/usr/bin/env python
# Module:   scipy_rand.py
# Purpose:  random distributions in SciPy
# Date:     N/A
# Notes:
# 1) ...
# Ref:  http://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.exponential
#
"""Random numbers and Numpy"""

import numpy as np
#import scipy as sp
#import matplotlib as mpl
import matplotlib.pyplot as plt
import random as r

def scipy_rand():
    """Random numbers and Numpy"""
    print "scipy_rand.py:  random numbers and numpy"

    ll = 1000
    print "create array with %d random numbers, list comprehension" % ll
    # -- example using Python's random
    # n1 = np.array([r.random() for x in range(ll)])
    n1 = np.random.random_sample((ll,))
    x1 = np.linspace(1, ll, ll)
    plt.plot(x1, n1)
    plt.grid()
    plt.show()

    print "make a histogram of the numbers and plot"
    bins = 10
    h1 = np.histogram(n1, bins)
    x10 = np.linspace(1, bins, bins)
    plt.plot(x10, h1[0])
    plt.show()

    print "redo with poisson distribution"

    print "create array with %d random numbers, list comprehension" % ll
    # -- example using Python's random
    # n2 = np.array([r.expovariate(1/5.0) for x in range(ll)])
    n2=np.random.exponential(scale=5, size=ll)
    #x1 = np.linspace(1, ll, ll)
    plt.plot(x1, n2)
    plt.grid()
    plt.show()

    print "make a histogram of the numbers and plot"
    #bins = 10
    h2 = np.histogram(n2, bins)
    #x2 = np.linspace(1, bins, bins)
    plt.plot(x10, h2[0])
    plt.show()

    print "Average of N2 is:  ", np.average(n2)

    print "use poisson and plot data then histogram"
    n3=np.random.poisson(lam=5.0, size=ll)
    plt.plot(x1, n3)
    plt.grid()
    plt.show()

    #bins = 10
    h3 = np.histogram(n2, bins)
    #x2 = np.linspace(1, bins, bins)
    plt.plot(x10, h3[0])
    plt.show()

    print "Average of N3 is:  ", np.average(n3)


if __name__ == "__main__":
    scipy_rand()
