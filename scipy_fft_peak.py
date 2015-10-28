#!/usr/bin/python
# Module:   scipy_fft_peak.py
# Purpose:  compute FFT and plot results
# Date:     N/A
# Notes:    
# 1)  Test python code
# 2)  This uses scipy and matplotlib, pkgs must be loaded
#     as they are not default....
# 3)  This uses peak estimation:
#      https://ccrma.stanford.edu/~jos/sasp/Quadratic_Interpolation_Spectral_Peaks.html
#
# std imports and set namespace
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

# allows us to find index of maximum
from numpy import argmax

print "scipy_fft_peak.py:  compute FFT, interpolate peaks, and plot points"
print ""

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

# freq per bin (typ this would be FS/N where FS = sample rate, N=bins)
df = xf[1]-xf[0]
  
# find peak in samples (use mag as max(yf) as values may be neg
# and max(yf) may not find the correct peak
zf=abs(yf)
fftmax_idx = argmax(zf)
fftmax_mag = zf[fftmax_idx]
fftmax     = yf[fftmax_idx]
print "Max=", fftmax, " mag=", fftmax_mag, " idx=", fftmax_idx

# get a,b,c
a=zf[fftmax_idx-1]
b=zf[fftmax_idx]
c=zf[fftmax_idx+1]
print "Mags[idx-1:idx+1]  a=", a, " b=", b, " c=", c

# interpolate the peak, magnitude, frequency
peak_idx=0.5*(a-c)/(a-2*b+c)
peak_mag=b - 0.25*(a-c)*peak_idx
peak_idx+=fftmax_idx + 1
peak_freq=df * peak_idx

print "peak_mag=", peak_mag, " peak_freq=", peak_freq, " peak_idx=", peak_idx

# plot using matplotlib -- apt-get install python-matplotlib
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
plt.grid()
plt.show()
