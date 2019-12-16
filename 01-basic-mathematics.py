# Covering the basic Mathematics that will be involved in learning about Audio Signal Processing

# SINUSOIDAL FUNCTION (i.e. a SINEWAVE) - 

# Is a mathematical curve that describes a smooth repetitve oscillation
# To plot a sinewave using Python you can do the following:

import numpy as np

A = .8                                    # The Amplitude value 
f0 = 1000                                 # The frequency, 1000 hertz
phi = np.pi / 2                           # The intitial phase (phi) at time zero
fs = 441000                               # The sample rate used for the time array
t = np.arange(-.002, .002, 1.0/fs)        # The time array used to generate the function, time from -.002 seconds to .002 seconds, sampled at the sample rate fs

x = A * np.cos(2 * np.pi * f0 * t + phi)  # The sinewave function (x)


