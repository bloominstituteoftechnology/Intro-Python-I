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
    """ math.sqrt(x): Return the square root of x"""
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
"""dist(a, b) caluculate the distance and format shows just 2 decimals"""
print("Distance is: {:.2f}".format(dist(a, b)))


# Write a function `print_tuple` that prints all the values in a tuple
# YOUR CODE HERE


def print_tuple(tupl):
    """"function that unpack the tuple and print each element""""
    for x in tupl:
        print(x)

t = (1, 2, 5, 7, 99)
# Prints 1 2 5 7 99, one per line
print('Tuple t: ')
print_tuple(t)

# Declare a tuple of 1 element then print it
"""
Using u(1) we have this error:
TypeError: 'int' object is not iterable
"""

# What needs to be added to make this work?
"""
To write a tuple with a single element
we have to include a comma after the element
"""
print('Tuple u: ')
u = (1,)
print_tuple(u)
