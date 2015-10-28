#!/usr/bin/env python
# Module:   lambda1.py
# Purpose:  lambda function test
# Date:     N/A
# Notes:    
# 1)  Test python code, based on ref below.
# Ref:  http://www.secnetix.de/olli/Python/lambda_functions.hawk

print "lambda1.py:  test of Python's lambda functions"

# very simple lambda function to square value
print "Simple lambda to square value"
g = lambda x: x**2
print g(8)

# example of anonymous function with initializer 
print
print "Create anon function to increment value"
print "(This makes more or less a prototype function.)"
def make_inc (n): return lambda x: x + n
f = make_inc(2)
g = make_inc(3)
print "test mi(2,42) ", f(42)
print "test mi(3,42) ", g(42)


print
print "Examples of filter, map, reduce"
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print "input:   ", foo
print "filter:  ", filter(lambda x: x % 3 == 0, foo)
print "map:     ", map(lambda x: x * 2 + 10, foo)
print "reduce:  ", reduce(lambda x, y: x + y, foo)

print
print "Compute primes 0..50 using sieve of Eratosthenes:"
nums = range(2, 50) 
for i in range(2, 8): 
  nums = filter(lambda x: x == i or x % i, nums)
print nums

print
print "Split sentence then print length each word:"
sentence = 'It is raining cats and dogs'
print "input:    ", sentence
words = sentence.split()
print "words:    ", words
# ['It', 'is', 'raining', 'cats', 'and', 'dogs']

lengths = map(lambda word: len(word), words)
print "lengths:  ", lengths
# [2, 2, 7, 4, 3, 4]

print "Example of commands splitting mount points:"
import commands
mount = commands.getoutput('mount -v')
lines = mount.splitlines()
points = map(lambda line: line.split()[2], lines)

print points

print "Points mapped in single line:"
print map(lambda x: x.split()[2], commands.getoutput('mount -v').splitlines())
#['/', '/var', '/usr', '/usr/local', '/tmp', '/proc']

print "Points via split"
lines = commands.getoutput('mount -v').splitlines()
points = map(lambda line: line.split()[2], lines)
print points

print "Points via for"
lines = commands.getoutput('mount -v').splitlines()
points = [line.split()[2] for line in lines]
print points

