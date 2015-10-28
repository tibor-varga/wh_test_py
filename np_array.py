#!/usr/bin/env python
# Module:   np_array.py
# Purpose:  Numeric Python arrays
# Date:     N/A
# Notes:
# 1) http://docs.scipy.org/doc/numpy/reference/arrays.html
# 2) Numpy arrays requre length to be set UP FRONT so can't
#    be easily extended like python lists (you can append 
#    but it creates a new list).

import numpy as np

#------------------------------------------------------------
# function for use with np.fromfunction()
def AFunc(x, y):
    return(x+y)

#------------------------------------------------------------
print "np_array.py:  Numpy array tests"
print "Creating tuple t3 with some int and float values"
t3=(1, 2, 3, 4, 5, 6, 7, 8, np.pi)

print "Converting to a Numpy array directly"
a1 = np.array(t3)
print a1
print "values:  [0]=%f, [1]=%f, [2]=%f" % (a1[0], a1[1], a1[2])

print "Converting to a list then to a Numpy array"
l3 = list(t3)
a2 = np.array(l3)
print a2

print "Extending the list, making it go to 11 (->new list)"
a2a=np.append(a2, 11)
print a2a

print "Creating empty list"
a3 = np.empty(0)
print a3

print "Creating a 2x3 array of integers"
a4=np.zeros((2,3), dtype=np.int)
print a4

print "...setting some values"
a4[0,1]=2
a4[1,2]=3
print a4

print "Info on a4:"
print "  array shape=", a4.shape
print "  array dimensions=", a4.ndim
print "  buffer=", a4.data
print "  elements=", a4.size
print "  dtype=", a4.dtype

print "Flatten the array to 1D and then compute sum"
a4f=a4.flat
a4fl=len(a4f)
sum=0
for i in range(0, a4fl):
    sum += a4f[i]
print "SUM=", sum, "NP sum=", np.sum(a4)

print "Creating with arange, float"
a5=np.arange(2,4,.1, dtype=np.float)
print a5

print "Creating with linspace"
a6=np.linspace(0.0, 1.01, 11)
print a6


print "Creating from a function AFunc"
a7=np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
print a7
print "Values[0,1]=%d [0,2]=%d\n" % (a7[0,1], a7[0,2])

a8=np.fromfunction(AFunc, (3,3))

ll=10.0
print "Creating from a list context, note [function for x in range()] syntax"
a9=np.array([np.cos(x/ll*2*np.pi) for x in range(0,int(ll))])
print a9

# This will work with an iterator, the -1 says consume all from
# the generator so it only works if the generator has a finite size.
# Specify COUNT to only generate N elements from a generator.
#    np.fromiter(g,np.float,COUNT) 
print "Creating from a generator:"
g=(np.cos(x/ll*2*np.pi) for x in range(0,int(ll)))
a9a=np.fromiter(g,np.float,-1)
print a9a

print "Creating a simple array and reshaping it, then iterating"
a10 = np.arange(6).reshape(2,3)
print "a10=", a10
# -- order is chosen to match memory layout, typ. C layout
for x in np.nditer(a10):
    print x,

print "\nCreating transpose"
a11=a10.T
for x in np.nditer(a11):
    print x,

print "Add 1 to each element using nditer."
print "  Note that nditer is typically readonly, hence use readwrite."
print "  Note also that x[...] must be used to change the array element."
a11[0,1]=7
for x in np.nditer(a11, op_flags=['readwrite']):
    x[...]=x+1
    print x,
print

print "Done!"




