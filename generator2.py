#!/usr/bin/env python
# Module:   generator2.py
# Purpose:  sample generator classes #2
# Date:     N/A
# Notes:    
# 1)  Test python code
# 2)  Ref:  https://docs.python.org/2/reference/expressions.html

import numpy as np

print "generator2.py:  python generator test code #2"

# echo from the generator examples
# - any function with yield in it becomes a generator
# - methods are next(), send(), throw(), and close()
def echo(value=None):
    print "Execution starts when 'next()' is called for the first time."
    try:
        while True:
            try:
                value = (yield value)
            except Exception, e:
                value = e
    finally:
        print "Don't forget to clean up when 'close()' is called."

print "testing the echo generator from examples"
g=echo(1)
v=g.next()
print "g.next()=", v
v=g.next()
print "g.next()=", v
g.throw(TypeError, "test")

print "Sending 2: ", g.send(2)
print "g.next()=", g.next()
print "Closing g"
g.close()

# test generator, return n*gv (typ 
def g1(iv=1, gv=0.9):
    iiv=iv
    print "g1() created, iv=%f, gv=%f" % (iv, gv)
    try:
        while True:
            try:
                # compute next value for the loop
                iiv=iiv*gv

                # print "iiv=", iiv
                if (iiv < 1):
                    break

                # set xv if user calls send(n)
                xv = yield iiv

                # if xv is sane, change the loop number
                if (xv != None):
                    print "g1() setting to ", xv
                    iiv=xv
            except Exception, e:
                yield e
    finally:
        print "g1() done, call close()"

print "Creating g1(10) generator and testing"
g=g1(10)
for x in g:
    print "x=", x
g.close()

print "Creating g1(7) and using next() and send()"
g=g1(7)
x=g.next()
print "g.next()= ", x
print "g.next()= ", g.next()
x=g.send(3)
print "g.send(3)=", x
print "g.next()= ", g.next()
print "g.next()= ", g.next()


print "numpy generator:  g=(np.cos(x) for x in np.arange(0, 10, .1))"
g=(np.cos(x) for x in np.arange(0, 10, .1))
print "g.next()=", g.next()
print "g.next()=", g.next()
print "g.next()=", g.next()
