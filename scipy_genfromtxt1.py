#!/usr/bin/env python
# Module:   scipy_genfromtxt1.py
# Purpose:  generate data form text 
# Date:     N/A
# Notes:
# 1) This is a simple test of genfromtxt used to read CSV data. 
# Ref:  http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html
#
import numpy as np
from StringIO import StringIO
#
d_in = "1,a,aa\n2,b,bb\n3,c,cc"
print d_in
res = np.genfromtxt(StringIO(d_in), dtype="i4,S1,S2", delimiter=",")

print "Result=", res
