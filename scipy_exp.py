#!/usr/bin/env python
# Module:   scipy_exp.py
# Purpose:  scipi test program w/ exponential dist.
# Date:     N/A
# Notes:
# 1) From the scipy examples....
#
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.stats import expon

CNT=1000

r = expon.rvs(size=CNT)
x=np.linspace(0,CNT-1, CNT)
h = plt.plot(x, r)
plt.show()

fig, ax = plt.subplots(1, 1)
ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
plt.show()
