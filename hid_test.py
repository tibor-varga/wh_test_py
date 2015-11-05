#!/usr/bin/python
# Module:   hid_test.py
# Author:   Wade Hampton
# Date:     n/a
# Notes:
# 1)  This requires the hidapi module and the hid lib to be loaded.
#     - load hid module, tested on Ubuntu:
#         apt-get install install libhidapi-libusb0
#         [includes keyboard support]
#         [alt is libhidapi-hidraw0 for raw devices]
#     - get the Python module:  https://pypi.python.org/pypi/hid/0.1.1
#     - extract and install the python module
#         tar xvzf hid-0.1.1.tar.gz
#     - install (root)
#         cd hid-0.1.1
#         python setup.py install
# 2)  Plug in a HID USB device and run this program
#     - if device is raw, you might be able to open by path
#     - use vid/pid for non-raw devices (works for keyboards)
# 3)  This may need to be run as root unless you change the
#     permissions on the HID device....
#

import hid

# get list of HID devices connected to this computer
h=hid.enumerate()
print "HID info=", h

# get path of first item
item=0
path=h[item]['path']
vid=h[item]['vendor_id']
pid=h[item]['product_id']

print "Path=%s Vid=%s Pid=%s" % (path, vid, pid)

# open the device
try:

# using path works on raw, not non-raw
#    d=hid.Device(path=path)
#    print "Opened device=", path

    d=hid.Device(vid=vid, pid=pid)
    print "Opened device=", vid, pid

    # -- TBD
    #r=d.get_feature_report(1, 1024)
    #print "Report=", r

    # loop rading the keyboard....
    done=0
    while(done==0):
        r=d.read(10)
        for c in r:
            x=ord(c)
            print "read=",x
        
except Exception, e:
    print "Exception, e=", e

print "Done!"
