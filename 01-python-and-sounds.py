# Importing the read function from the scipy module wavFile in the module IO
# Takes an input of a file path as string, and returns as the out the sample Rate and an array of sound samples
from scipy.io.wavfile import read
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np

(fs, x) = read('./audio/flute-A4.wav')

print(fs)
# Output: 44100

print(x)
# Output: [  0  -2   3 ..., -19 -10 -13]
# Which is an array of 16 bit integers, incl. all samples,
# displaying only the first and last 3 entries

print(x.size)
# Output: 94803

# To find out how many seconds 94803 samples is, you can divide the number of samples into the sample rate
print(x.size / fs)
# Output: 2

# These two numbers are integers, so the result is an integer
# To know the duration exactly you can use float() to convert one of these numbers into a floating point number
print(x.size / float(fs))
# Output: 2.14972789116
# So, 2.149 seconds

# Now you can plot the sound by using the imported matplotlib.pyplot module above
plt.plot(x)
plt.show()

# In order to visualise the sound not using the integer values -10,000 -> 8,000, but rather using a time value like seconds
# You can use the numpy module to define a time axis
# Using the numpy function arange(), this creates a new array going from zero up to the length that you input, which here is (x.size)
timeAxis = np.arange(x.size)/float(fs)
# Then by dividing by the sample rate you will get the exact duration in seconds, like how it was done above with print(x.size / float(fs))

# Plot the new visualisation using array timeAxis with respect to x
plt.plot(timeAxis, x)

# Will show the same visualisation as above only with the X axis using the seconds values from timeAxis (0 -> 2.5)
plt.show()

# There are also python commands used to show specific samples from this array:

y = x[44100:45100]
# Take a selection of 1000 samples
plt.plot(y)
plt.show()

# Using the numpy max() function to get the max value of the array
print(np.max(y))
# Output: 4511

# BUT because sound oscillates around zero, this array will have positive and negative values
# SO it would make more sense to take the absolute value of y, which means also taking the negative values into consideration

print(np.max(abs(y)))
# Output: 7132
# This number was a negative value that was higher in terms of absolute value

# You can also use the sum() function to sum all of the values in an array
print(np.sum(y))
# Output: -37359
# It is negative because the array has negative values, as sound samples oscillate around 0


# However you can also use abs() again the return the summed absolute values
print(np.sum(abs(y)))
# Output: 3073713


# Using the WRITE function imported from the IO/wavFile scipy module
# you can create a new wav file. The function takes an input of a file path to write, a sample rate to use (fs, read from flue-A4)
# and then an array of numbers, here using (y) the slice of 1000 samples from (x)
write('./audio/test.wav', fs, y)