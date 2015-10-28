#!/usr/bin/python
# Module:   scipy_fft.py
# Purpose:  compute FFT and plot results
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

print "scipy_fft.py:  compute FFT and plot points"

# fft example
from scipy.fftpack import fft
# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 800.0

# create input array of samples of 2 sines
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

# compute the FFT and convert to a linear array
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

# plot using matplotlib -- apt-get install python-matplotlib
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.grid()
plt.show()
