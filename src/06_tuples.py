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
def print_tuple(t):
    for item in t:
        print(item)    

t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
u = (1,)  # What needs to be added to make this work?
print_tuple(u)


# destructing tuples
x = 1, 2
print(x)
print(type(x))

def return_multiple():
    return 1,2

a = return_multiple()
print(a)

c, d = x
print(c)
print(d)

x,y = 3, 5
print(x)
print(y)

x, y = (3,4)

# if you had a dictionary in a tuple can you edit the dictionary? Or is everything within immutable?

my_dict = {'a' :1, 'b': 2}

my_tuple =(1,2, my_dict)

my_tuple = (1,2, my_dict)
print(my_tuple)

my_dict['a'] = 3

print(my_tuple)

# my_tuple[2] = {}

my_new_tuple = (1, 2, {"a": 1, 'b': 3})

my_new_tuple[2]['a'] = 4

print(my_new_tuple)

my_new_tuple[2]['c'] = 99
print(my_new_tuple)

my_third_tuple = (1, 'a', [1,2])
my_third_tuple[2].append(3)
print(my_third_tuple)

# passing by reference and passing by value

x = [1,2,3]

y = x

print(x)
print(y)

y.append(4)
print(x)

y = None
print(x)
print(y)

x = 1
print(1)

y = x
print(y)

y *= 2
print(y)

print(x)