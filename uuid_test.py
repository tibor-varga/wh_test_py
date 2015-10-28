#!/usr/bin/env python
# Module:   uuid_test.py
# Purpose:  generate UUIDs
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/uuid.html
#
#
import uuid
import time

print "uuid_test.py:  test of UUIDs"

ts=time.clock()
node=uuid.getnode()
print "Node=", node
myuuid=uuid.uuid1(node)
s=str(myuuid)
print "UUID=%s" % s

# manually specify a node
node=0x1234567890
print "Node=", node
myuuid=str(uuid.uuid1(node))
print "UUID=%s" % myuuid

# manually specify a time
node=0xabcdef123456
print "Node=", node
clk=int(100000*time.time())
print "Clk= ", clk
myuuid=str(uuid.uuid1(node, clk))
print "UUID=%s" % myuuid

print "Done!"
# 
#import ctypes
#cb = ctypes.create_string_buffer(16)
