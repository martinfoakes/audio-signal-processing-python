# PYTHON - Is a high level programming language

# To deal with array operations etc. you can use numpy package, imported here with the alias name np
import numpy as np

# To handle array plotting you sue matplotlib, specifically the module pyplot that handles dimensional plotting
import matplotlib.pyplot as plt

# Now with numpy imported you have access to its functions
# Declaring a variable, using the numpy function array() to create an array:
a = np.array([0, 1, 2, 3, 4, 5])

# Accessing individual elements of the array, or a range of elements:

print(a[3])
# Output: 3

print(a[0:4])
# Output: [0 1 2 3]

# The plotting of this arraying using matplotlib's pyplot module

# Plot function, generates a display object
plt.plot(a)

# Command that shows the generated display object
plt.show()

# Making a new variable that is the reversed array of (a)
# :: is accessing all the indexes of the array (a) and icnrementing by -1
b = a[::-1]

print(b)
# Output [5 4 3 2 1 0]