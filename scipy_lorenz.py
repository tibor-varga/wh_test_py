#!/usr/bin/env python
# Module:   scipy_lorenz.py
# Purpose:  Lorenz attractor solved and plotted (Numpy/Matplotlib)
# Date:     N/A
# Notes:
# 1) Lorenz Attractor solved using NP's ODE solver and plotted 
#    using Matplotlib's 3d plot.
# 
# 2) Ref:  
#    https://en.wikipedia.org/wiki/Lorenz_system
#    http://wiki.scipy.org/Cookbook/Zombie_Apocalypse_ODEINT
#    http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
#
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

# setup defaults, see wikipedia article
rho=28
sigma=10
beta=8/3

# function to solve 
def lorenz(y, t):
    #  f = @(t,a) [-sigma*a(1) + sigma*a(2); 
    #               rho*a(1) - a(2) - a(1)*a(3); 
    #               -beta*a(3) + a(1)*a(2)];

    f0 = -sigma * y[0] + sigma * y[1]
    f1 = rho * y[0] - y[1] - y[0]*y[2]
    f2 = -beta * y[2] + y[0]*y[1]

    return(f0, f1, f2)

# define initial conditions
y0 = [1,1,1]
t = np.linspace(0, 100, 10000)

soln = odeint(lorenz, y0, t)
a = soln[:, 0]
b = soln[:, 1]
c = soln[:, 2]

# plot each versus time, not very interesting
#plt.figure()
#plt.plot(t, a, label='A')
#plt.plot(t, b, label='B')
#plt.plot(t, c, label='C')
#plt.xlabel('Time')
##plt.ylabel('A')
#plt.title('Lorenz Attractor')
#plt.legend(loc=0)
#plt.show()

# plot a/b versus time as 3D, nice if rotated
fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
ax = fig.gca(projection='3d')
ax.plot(a, b, t, label='versus time')
plt.show();

# plot a/b/c in 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(a, b, c, label='Lorenz Attractor')
plt.show();
