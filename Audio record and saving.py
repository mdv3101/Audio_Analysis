# -*- coding: utf-8 -*-
"""
This code will record an audio and store it in numpy array. 
It will then ask the user to enter it's name which could be use as file name.
Created on Sun Jun 25 17:31:18 2017

@author: Madhav
"""

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from scipy.io.wavfile import write
CHANNELS = 2
RATE = 44100
fs=44100
duration = 5  # seconds
myrecording = sd.rec(duration * fs, samplerate=fs,channels= CHANNELS,dtype='float64')
print ("Recording Audio")
sd.wait()
print ("Audio recording complete , Play Audio")
sd.play(myrecording, fs)
sd.wait()
form = ".wav"
name = input("Enter your name:")
name = name+form
print(name)
write(name, 44100, myrecording)
print ("Audio saving Complete")
