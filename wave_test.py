#!/usr/bin/env python
# Module:   wave_test.py
# Purpose:  python wave I/O to create sample wave file with 1K tone
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/wave.html
#    http://soledadpenades.com/2009/10/29/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/
#    https://docs.python.org/2/library/struct.html
# 2) More features can be found using the Libsndfile module for
#    Python (not included in the core distribution).
# 3) Test using "play", you should hear a pure 1K tone:
#      play test.wav
#
from math import cos, pi
import wave as w
import sys
import struct

# define wave parameters
bits=16
sps=16000
chan=1
dur=10  # seconds

# for tone generation
freq=1000.0   # Hz
vol=32768-2000  # 32768 is max
k = 2.0 * pi * freq / sps

ofile="test.wav"

print "wave_test.py:  test of Wave file handling"
print "creating wave file with bits=", bits, "SPS=", sps, "chan=", chan, "dur=",dur, "sec"

# handle exceptions opening and setting up the wave file
try:
    wf = w.open(ofile, 'wb')
    # can do this with one call....
    wf.setnchannels(chan)
    wf.setsampwidth(bits/8)
    wf.setframerate(sps)

    # generate audio using cos() function
    for i in range(0, dur*sps):
        s = vol*cos(i*k)
        # pack python values to raw data, machine native format (Intel)
        # key "h" indicates a short integer, std size is 2 bytes as expected
        pv = struct.pack('h', s)
        wf.writeframes(pv)

    wf.close()

except Exception, e:
    print "Exception, e=", e
    sys.exit(1)

print "Done!"
