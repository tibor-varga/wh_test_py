#!/usr/bin/python
# Module:   scipy_wav_test.py
# Purpose:  test reading wave files
# Date:     N/A
# Notes:    
# 1)  Test python code
# 2)  Use SOX to generate a test wave file, linear, 8KSPS, 1000HZ+1001HZ mix
# 2)  Read the wave file using scipy.  Note this complains reading uLaw so
#     the input file is converted to linear.
# 3)  Plot the file.
#
import subprocess
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io.wavfile
import math
#
print "scipy_wav_test.py:  generate and process wave files"
print "use SOX to generate files (cleanup.py will cleanup)"
print "  output-> mix.wav, uLaw WAVE file, 5S, 8000SPS, 1000+1001 Hz"
subprocess.call('sox -n -r 8000 -e mu-law f1001.wav synth 5 sine 1001 vol -3 dB', shell=True)
subprocess.call('sox -n -r 8000 -e mu-law f1000.wav synth 5 sine 1000 vol -3 dB', shell=True)
# -- uLaw not supported by scipy so use linear....
#subprocess.call('sox --combine mix f1000.wav f1001.wav mix.wav', shell=True)
subprocess.call('sox --combine mix f1000.wav f1001.wav -b 16 -e signed-integer mix.wav', shell=True)

rate,wav_data=sp.io.wavfile.read("mix.wav")
print wav_data

x=np.linspace(0.0,len(wav_data)-1, len(wav_data))
plt.plot(x,wav_data)
plt.grid()
plt.show()

