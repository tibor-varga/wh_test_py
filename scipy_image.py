#!/usr/bin/env python
# Module:   scipy_image.py
# Purpose:  Image test from examples (header added)
# Date:     N/A
# Notes:
# 1) from examples
# Ref: http://docs.scipy.org/doc/scipy/reference/tutorial/signal.html 

import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

# import the image -- pre-defined
image = misc.lena().astype(np.float32)

# filter the image
derfilt = np.array([1.0, -2, 1.0], dtype=np.float32)
ck = signal.cspline2d(image, 8.0)
deriv = (signal.sepfir2d(ck, derfilt, [1]) +
         signal.sepfir2d(ck, [1], derfilt))

laplacian = np.array([[0,1,0], [1,-4,1], [0,1,0]], dtype=np.float32)
deriv2 = signal.convolve2d(ck,laplacian,mode='same',boundary='symm')

# plot the original
plt.figure()
plt.imshow(image)
plt.gray()
plt.title('Original image')
plt.show()

# plot the edge filter
plt.figure()
plt.imshow(deriv)
plt.gray()
plt.title('Output of spline edge filter')
plt.show()

