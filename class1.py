#!/usr/bin/env python
# Module:   class1.py
# Purpose:  class test #1 -- very basic class syntax in Python
# Date:     N/A
# Notes:
# 1)  Test python code
#
"""class test 1, very basic class syntax in Python"""

# define the base class
class MyBase:
    """very basic test class"""
    def __init__(self, a, b, c):
        """create the very basic test class with 3 numbers, a,b,c """
        self.a = a
        self.b = b
        self.c = c
        # end w/ comma so no newline
        #print "MyBase init:",
        #self.xprint()

    def empty(self):
        """empty the class, set all to 0"""
        self.a = self.b = self.c = 0
        return 0

    def add(self):
        """add all three numbers in the class, return sum"""
        res = self.a + self.b + self.c
        return res

    def xprint(self):
        """print the info in the class"""
        print "(", self.a, ",", self.b, ",", self.c, ")"


# define derived class 1 (subclass inheriting from MyBase)
class MyDerived(MyBase):
    """derived class from the basic test class 1"""
    def __init__(self, name_in, a=0.0, b=0.0, c=0.0):
        """create the derived class with name plus 3 numbers"""
        self.xname = name_in
        MyBase.__init__(self, a, b, c)
        #print "my_derived init:",
        #self.xprint()

    def xprint(self):
        """print the derived class, call the base print as well"""
        print self.xname,
        MyBase.xprint(self)


# class derived from a standard class, complex
class MyComplex(complex):
    """new complex class derived from the standard complex class"""
    def __init__(self, ri, ii):
        """create the new complex class, pass real, imag parts"""
        self.r = ri
        self.i = ii
        self.z = complex(ri, ii)
        complex.__init__(self, ri, ii)

    def xprint(self):
        """print the new complex class"""
        print "R=", self.r, " I=", self.i
        print "Z=", self.z
        print "RI=", self.z.real, "+i", self.z.imag
        print "abs=", self.abs()

    def abs(self):
        """return abs() of the new complex class"""
        res = abs(self.z)
        return res


# main code
print "class1.py:  test of Python classes #1"

print "Test 1 of complex class "
mc = MyComplex(1, 2)
mc.xprint()


print "Test 2 of base class "
mb = MyBase(1, 2, 3)
mb.xprint()

print "added=", mb.add()

print "Test 3 of derived class"
md = MyDerived('asdf', 1, 2, 4)
md.xprint()
