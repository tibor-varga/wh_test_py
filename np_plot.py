#!/usr/bin/env python
# Module:   np_plot.py
# Purpose:  simple plot and complex plot using np
# Date:     N/A
# Notes:
# 1) Simple plots
#
import numpy as np
#import matplotlib as mpl
import matplotlib.pyplot as plt

print "np_plot.py:  some simple plots"

print "dumb assignment to numpy array"
# -- better would be to use an iterator, see other examples
ll=10.0
z=np.zeros(int(ll))
x=np.linspace(0.0,np.pi/ll, ll)
for i in range(0,int(ll)):
    z[i]=np.cos(np.pi*i/ll)
    
plt.plot(x,z)
plt.grid()
plt.show()

print "array assignment using list context"
z=np.array([np.cos(np.pi*i/ll) for i in range(0,int(ll))])
plt.plot(x,z)
plt.grid()
plt.show()

