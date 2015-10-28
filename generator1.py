#!/usr/bin/env python
# Module:   generator1.py
# Purpose:  sample generator classes
# Date:     N/A
# Notes:    
# 1)  Test python code
print "generator1.py:  python generator test code"

print "define generator of N=0..9"
g=(xrange(0,10))

for x in g:
  print "val=", x

print "define generator of square roots"
g=(x**.5 for x in xrange(0,10))
for x in g:
  print "val=", x

# very verbose iterator
# from:  http://wiki.python.org/moin/Generators
class firstn(object):
  def __init__(self, n):
      self.n = n
      self.num, self.nums = 0, []
  def __iter__(self):
      return self
  # next method -- required, called for each iteration
  def next(self):
      if self.num < self.n:
          cur, self.num = self.num, self.num+1
          return cur
      else:
          raise StopIteration()

max=1000000
sum_of_first_n = sum(firstn(max))
print "sum of first (", max, ") = ", sum_of_first_n


# simpler iterator
print "a generator that yields items instead of returning a list"
def firstn1(n):
   num = 0
   while num < n:
     # equivalent of next(), return the value, save state
     yield num
     num += 1
sum_of_first_n = sum(firstn1(max))
print "sum of first (", max, ") = ", sum_of_first_n
 
print
print "list comprehension"
doubles = [2 * n for n in range(50)]
print "doubles=", doubles
 
print
print "same as the list comprehension above"
doubles = list(2 * n for n in range(50))
print "doubles=", doubles

import unittest

# print "irange as a RangeGenerator, vs xrange which is a lazy list "
