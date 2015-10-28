#!/usr/bin/python
# Module:   scipy_ring.py
# Purpose:  ringing cos
# Date:     N/A
# Notes:    
# 1)  Test python code
# 2)  This uses scipy and matplotlib, pkgs must be loaded
#     as they are not default....
#
# std imports and set namespace
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import pi

print "scipy_ring.py:  numpy test code with ringing cos() fcn"
x=np.linspace(0.0,999,1000)
y=np.cos(2*pi*x/50)*np.cos(0.5*pi*x/len(x))

plt.plot(x,y)
plt.grid()
plt.show()

y=np.cos(2*pi*x/50)*np.cos(2*pi*x/len(x))
plt.plot(x,y)
plt.grid()
plt.show()
