#!/usr/bin/env python
# Module:   scipy_filt1.py
# Purpose:  
# Date:     N/A
# Notes:
# 1) ...
# Ref:  any references
#  http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.signal.iirfilter.html
"""Docstring for top-level"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

b, a = signal.iirfilter(17, [50, 200], rs=60, btype='band', analog=True, ftype='cheby2')

w, h = signal.freqs(b, a, 1000)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(w, 20 * np.log10(abs(h)))
ax.set_xscale('log')
ax.set_title('Chebyshev Type II bandpass frequency response')
ax.set_xlabel('Frequency [radians / second]')
ax.set_ylabel('Amplitude [dB]')
ax.axis((10, 1000, -100, 10))
ax.grid(which='both', axis='both')
plt.show()

