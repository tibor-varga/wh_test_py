#!/usr/bin/env python
# Module:   class1.py
# Purpose:  class test 
# Date:     N/A
# Notes:    
# 1)  Test python code
#
# define the base class
class my_base:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    # end w/ comma so no newline
    print "my_base init:",
    self.xprint()

  def empty(self):
    self.a = self.b = self.c = 0
    return(0)

  def count(self):
    res = self.a + self.b + self.c
    return(res)

  def xprint(self):
    print "(",self.a,",",self.b,",",self.c,")"
     

# define derived class 1

# class derived from std class
class my_complex(complex):

  def __init__(self, ri, ii):
    self.r = ri
    self.i = ii
    self.z = complex(ri, ii)

  def xprint(self):
    print "R=", self.r, " I=", self.i
    print "Z=", self.z
    print "RI=", self.z.real, "+i", self.z.imag
    print "abs=", self.abs()

  def abs(self):
    res = abs(self.z)
    return(res)


# main code 
print "class1.py:  create a test class"
mc = my_complex(1,2)
mc.xprint()


mb = my_base(1,2,3)
mb.xprint()
