#!/usr/bin/env python
# Module:   hanning.py
# Purpose:  Hann or Hanning or Raised Cosine window
# Date:     N/A
# Notes:
# 1) Reference:
#      http://docs.scipy.org/doc/numpy/reference/generated/numpy.hanning.html
#      https://ccrma.stanford.edu/~jos/sasp/Matlab_Hann_Window.html
#
# 2)  From CCRMA:
#       M=3, range is 0..2 or range(0,3)
#       hanning(3) = w = .5*(1 - cos(2*pi*(1:M)'/(M+1))) -- remove the 0's
#       hann(3) = w = .5*(1 - cos(2*pi*(0:M-1)'/(M-1)));
#         same as np.hanning(3)
#
import numpy as np

M=3
r=r=np.r_[range(0,M)]
print "M=", M, "test using math for hann/hanning and using np.hanning()"
w1=0.5*(1-np.cos(2*np.pi*(r+1)/(M+1)))
w2=0.5*(1-np.cos(2*np.pi*r/(M-1)))
w3=np.hanning(M)
print "hanning(",M,"):     ", w1
print "hann(",M,"):        ", w2
print "np.hanning(",M,"):  ", w3

M=10
r=r=np.r_[range(0,M)]
print "M=", M, "test using math for hann/hanning and using np.hanning()"
w1=0.5*(1-np.cos(2*np.pi*(r+1)/(M+1)))
w2=0.5*(1-np.cos(2*np.pi*r/(M-1)))
w3=np.hanning(M)
print "hanning(",M,"):     ", w1
print "hann(",M,"):        ", w2
print "np.hanning(",M,"):  ", w3

# window width
M=256
# Number of samplepoints
N = M*6
# sample spacing
T = 1.0 / (4*M)

print "testing and plotting"

print "creating a window of", M, "points"
r=np.linspace(0,M)
w=np.hanning(M)

# create input array of samples of 1 sine
x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) 

# create rectangle window and hamming window 
yy=y[0:M]
yyh=w*yy

# compute the FFT and convert to a linear array
from scipy.fftpack import fft

yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
yyf = fft(yy)
xyf = np.linspace(0.0, 1.0/(2.0*T), M/2)
yyhf = fft(yyh)
xyhf = np.linspace(0.0, 1.0/(2.0*T), M/2)

# plot using matplotlib -- apt-get install python-matplotlib
import matplotlib.pyplot as plt
fig, (p1, p2) = plt.subplots(nrows=2)
p1.plot(xyf,np.abs(yyf[0:M/2]),'b-')
p1.set_title('Rectangle')
p2.plot(xyf,np.abs(yyhf[0:M/2]),'g-')
p2.set_title('Hamming')
plt.grid()
plt.show()
