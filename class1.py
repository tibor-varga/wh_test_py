#!/usr/bin/env python
# Module:   class1.py
# Purpose:  class test #1 -- very basic class syntax in Python 
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
    #print "my_base init:",
    #self.xprint()

  def empty(self):
    self.a = self.b = self.c = 0
    return(0)

  def add(self):
    res = self.a + self.b + self.c
    return(res)

  def xprint(self):
    print "(",self.a,",",self.b,",",self.c,")"
     

# define derived class 1 (subclass inheriting from my_base)
class my_derived(my_base):
  def __init__(self, name_in, a=0.0, b=0.0, c=0.0):
    self.xname = name_in
    my_base.__init__(self, a,b,c)
    #print "my_derived init:",
    #self.xprint()
    
  def xprint(self):
    print self.xname,
    my_base.xprint(self)


# class derived from a standard class, complex
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
print "class1.py:  test of Python classes #1"

print "Test 1 of complex class "
mc = my_complex(1,2)
mc.xprint()


print "Test 2 of base class "
mb = my_base(1,2,3)
mb.xprint()

print "added=", mb.add()

print "Test 3 of derived class"
md = my_derived('asdf', 1, 2, 4)
md.xprint()
