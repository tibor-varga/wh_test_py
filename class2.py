#!/usr/bin/env python
# Module:   class2.py
# Purpose:  class test #2 
# Date:     N/A
# Notes:    
# 1)  Test python code
#     https://docs.python.org/2/tutorial/classes.html

# simple class deriving from dict, showing doc and class variables
# - note that there is no data hiding/protection/private variables
# - note you can add to the class data attributes outside the class
# - by convention, a variable starting with _ should be treated as private
class xx1(dict):
    # define class variables shared by all instances
    """xx1 test class"""
    junk="xx1 junk"

    _p="PSEUDO-PRIVATE"

    # constructor:  define name of the class
    def __init__(self, name, x=0, y=0):
        self.name = name
        # self.x    = x
        # self.y    = y
        self.l    = []  # sample list
        self.__update(x, y, None)

    def add_l(self, item):
        self.l.append(item)

    # xprint:  create string and return it with lots of class data
    def xprint(self):
        return("XX1 %s %s %s" % (self.name, self.junk,self.__doc__))

    def sprint(self):
        return("%s %d %d %s" % (self.name, int(self.x), int(self.y), self.iprint()))

    def iprint(self):
        return(str(self.l))

    def getp(self):
        return(self._p)

    def update(self, x, y, item):
        self.add_l(item)
        self.x = x
        self.y = y

    __update = update  # private copy, name mangled

# define function outside the class, N+1 args, first is "self"
# - must define before defining in the class
def xp(k):
    return ('xp: nothing')

# very simple class demonstrating that "self" is custom, not a language feature
# -- in the below, the "self" is replaced by "k"
# -- use "self" in classes not like below as this is non-standard!
class j:
    f = xp  # define f as the function xp 
    def __init__(k,jj=0):
        k.jj=jj



# main code 
print "class2.py:  test of Python classes #2"


print "Test of simple class demonstrationg no use of \"self\""
jx=j(12)
print "jx.jj=", jx.jj
print "jx.f=", jx.f()
print "type of jj is ", jx.jj.__class__

print "Test simple class with list, print automatic dict in the class" 
x1=xx1("instance1")  # create an instance
x1.add_l('aa')
x1.add_l('bb')
x1.add_l(3.14)

print "Result=", x1.xprint()
print "Dictionary=", x1.__dict__
print "List=", x1.iprint()

print "Adding pi to x1 outside of x1"
x1.pi=3.14
print "Dictionary=", x1.__dict__

print "Pseudo-private _p:  ", x1.getp()

x1.update(22, 33, "ITEM")
print "Updating class:  ", x1.sprint()


print "Null class used as struct"
class Employee:
    pass

john = Employee() # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


print "values=", john.name, john.dept, john.salary
print "Dictionary=", john.__dict__

# same as john.dept:
print "...and dept=", john.__dict__['dept']


# simple class with an iterator, from examples
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        def __iter__(self):
            return self
        def next(self):
            if self.index == 0:
                raise StopIteration
            self.index = self.index - 1
            return self.data[self.index]

print "Create test object with iterator"
rev="This is a test"
ir=iter(rev)
print "Using Iter: ", ir.next()

print "Use in a FOR loop"
for char in rev:
    print "C=", char

