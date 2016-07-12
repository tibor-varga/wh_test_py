#!/usr/bin/env python
# Module:   fuzzy_test1.py
# Purpose:  test fuzzy string matching
# Date:     N/A
# Notes:
# 1) This uses the fuzzywuzzy module from GitHub as referenced
#    in several posts.  It can be used with or without the
#    python-Levenshtein C extension which makes it much faster
#    which could be very useful for large comparisons.
#
# 2) This only runs a few simple tests.
#
# 3) Ref:  
# https://github.com/seatgeek/fuzzywuzzy
# https://www.quora.com/Whats-a-good-Python-module-for-fuzzy-string-comparison
# https://marcobonzanini.com/2015/02/25/fuzzy-string-matching-in-python/
#
"""Fuzzy Test 1 -- test of fuzzy string matching"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def fuzzy_test1():
    """Perform fuzzy test 1"""
    print "fuzzy_test1:  test fuzzy string comparison"
    ST1 = "1234567890abcdef"
    ST2 = ST1
    r = fuzz.ratio(ST1, ST2)
    print "ST1={0}, ST2={1}, ratio={2}".format(ST1, ST2, r)

    ST2 = "123456780abcdef"
    r = fuzz.ratio(ST1, ST2)
    print "ST1={0}, ST2={1}, ratio={2}".format(ST1, ST2, r)

    ST2 = "1234zzzzzdef"
    r = fuzz.ratio(ST1, ST2)
    print "ST1={0}, ST2={1}, ratio={2}".format(ST1, ST2, r)

    ST2 = "fedzzzz987654321"
    r = fuzz.ratio(ST1, ST2)
    print "ST1={0}, ST2={1}, ratio={2}".format(ST1, ST2, r)

    ST2 = "zzzzzzzzzzzzzz"
    r = fuzz.ratio(ST1, ST2)
    print "ST1={0}, ST2={1}, ratio={2}".format(ST1, ST2, r)

if __name__ == "__main__":
    fuzzy_test1()
