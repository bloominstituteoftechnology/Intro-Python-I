"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use 
parens instead of square brackets. 

More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values 
never needs to be mutated, use a tuple instead of a list. 

Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically. 
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b
    
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))



# Write a function `print_tuple` that prints all the values in a tuple

# YOUR CODE HERE

t = (1, 2, 5, 7, 99)

def print_tuple(t):
  if type(t) == int:
    print(t)
  else:
    for n in t:
      print(n) # Prints 1 2 5 7 99, one per line


#curious, why doesn't this work?
#def print_tuple(t):
#  try:
#    for n in t:
#      print(n) # Prints 1 2 5 7 99, one per line
#  except TypeError:
#    print(n)

# Declare a tuple of 1 element then print it
u = (1)  # What needs to be added to make this work?
print_tuple(u)

#It appears that a tuple of length 1 assumes the variable type of whatever the lone item is,
#not that of a tuple. This means that a for loop for a tuple length of 1 will error out.
