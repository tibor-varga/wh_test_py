#!/usr/bin/env python
# Module:   lambda2.py
# Purpose:  lambda function test 2 with local-defined function
# Date:     N/A
# Notes:    
# 1)  Test python code
#     https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists
#     http://stackoverflow.com/questions/7745952/python-expand-list-to-function-arguments
#     
print "lambda2.py:  test of Python's lambda functions #2"

# very simple lambda function to square value
print "Simple lambda to convert mm to inches"
mmi = lambda x: x/25.4
print mmi(250)


# simple mm to inches scale function for 3 coord using the lambda
def scale (x, y, z):
    return(mmi(x), mmi(y), mmi(z))


# simple function in a function 
def funca(x,y,z):

    # define a function within a function (could use a lambda)
    def sqr(p):
        sq=p*p
        # could have more code here....
        return(sq)

    sum=x+y+z
    sumsqr=sqr(x)+sqr(y)+sqr(z)
    return (x+sumsqr, y+sumsqr, z+sumsqr)


# define some input values in mm, we will convert to inches
v=[250, 165, 140]
print "Input coordinates:  ", v

print "Expand the list into v:  X,Y,Z=v"
X,Y,Z=v
x,y,z = scale(X,Y,Z)
print "scale(X,Y,Z):  ",x,y,z

print "Unpack the arg list using *v, for dict use **d"
x,y,z = scale(*v)
print "scale(*v):     ",x,y,z

print "Result assigned to a sequence"
vs=scale(*v)
print "seq:   vs=     ", vs

print "Result converted to a list:"
vl=list(scale(*v))
print "list:  vl=     ", vl

print "Change coords with function with internal function"
vs=funca(*v)
print "res=           ", vs

vs=scale(*vs)
print "scaled=        ", vs
