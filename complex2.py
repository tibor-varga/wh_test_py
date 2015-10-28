#!/usr/bin/env python
# Module:   complex2.py
# Purpose:  Python test code
# Date:     N/A
# Notes:    
# 1)  Test python code to for complex numbers
# 2)  Use numpy to setup a floating point range as Python's
#     range is int only, and use matplotlib to plot the output.
# 3)  Ref:
#     https://docs.python.org/2/library/cmath.html
#     http://matplotlib.org/users/pyplot_tutorial.html
#     http://matplotlib.org/examples/color/named_colors.html
#
import cmath
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

PI=cmath.pi
E=cmath.e
R=10

# define a function E^-jwt
def xe(w,t):
    return(E**(-1.0j*w*t))

# compute a series of complex points and print them
#x=np.arange(0,2*PI,.1)
for x in np.arange(0,2*PI,.1):
    y=xe(100,x)
    print "X->Y", x, y

# use np to compute 100 points and 100 complex numbers
x=np.linspace(0,2*PI,100)
y=np.array(xe(100,x))

# create two sub-plots, 1 for real, 1 for imag
fig, (p1, p2) = plt.subplots(nrows=2)
p1.plot(x,y.real,'b-')  # color is BLUE
p1.set_title('Real values')
p2.plot(x,y.imag,'g-')  # color is GREEN
p2.set_title('Imag values')
plt.grid()
plt.show()

