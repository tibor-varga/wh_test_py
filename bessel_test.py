#!/usr/bin/env python
# Module:   bessel_test.py
# Purpose:  Numpy example
# Date:     ? (from references)
# Notes:
# 1) Requires numpy and matplotlib be installed on your system.
# 2) Makes a very nice surface plot.....
# 3) This is from the examples, Ref:
#    http://docs.scipy.org/doc/scipy/reference/tutorial/special.html
#
"""Numpy example of bessel functions from scipy tutorial"""

# standard numpy include
import numpy as np

# example code follows
from scipy import special
def drumhead_height(n, k, distance, angle, t):
    kth_zero = special.jn_zeros(n, k)[-1]
    return np.cos(t) * np.cos(n*angle) * special.jn(n, distance*kth_zero)

theta = np.r_[0:2*np.pi:50j]
radius = np.r_[0:1:50j]
x = np.array([r * np.cos(theta) for r in radius])
y = np.array([r * np.sin(theta) for r in radius])
z = np.array([drumhead_height(1, 1, r, theta, 0.5) for r in radius])

#print x
#exit(1)

# 3D surface plot of the results
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.jet)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

