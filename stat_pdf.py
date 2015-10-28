#!/usr/bin/env python
# Module:   stat_pdf.py
# Purpose:  test of shelve persisting objects 
# Date:     N/A
# Notes:
# 1) Reference:
#      http://wiki.scipy.org/Cookbook/Matplotlib/SigmoidalFunctions
#
from matplotlib.mlab import normpdf
#import matplotlib.numerix as nx <-- deprecated
import pylab as p

print "norm PDF from matplotlib"
x = p.arange(-4, 4, 0.01)
y = normpdf(x, 0, 1) # unit normal
p.plot(x,y, color='red', lw=2)
p.title("Norm PDF from matplotlib")
p.show()

print "norm PDF from scipy"
from scipy.stats import norm
x = p.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
p.plot(x, norm.pdf(x))
p.title("Norm PDF from scipy")
p.show()

print "norm CDF"
p.plot(x,norm.cdf(x))
p.title("Norm CDF from scipy")
p.show()

print "generating random numbers"
r = norm.rvs(size=10000)
p.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
p.title("Histogram of random numbers from norm.rvs()")
p.show()


