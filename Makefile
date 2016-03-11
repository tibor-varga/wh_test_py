#!/usr/bin/make
# Module:   Makefile
# Purpose:  make file for Python test, mainly cleanup
# Author:   Wade Hampton
# Date:     3/11/2016
# Notes:    
# 1) This file mainly exists to clean up after running
#    tests and examples.  The cleanup script removes
#    sample data files, outputs, etc.
#
all::
	$(MAKE) README

README::
	a2x -d article -f xhtml README.md

clean::
	./cleanup.py

cleanup::
	./cleanup.py

