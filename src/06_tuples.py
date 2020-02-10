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
def print_tuple(tt):
    if type(tt) is tuple:
        for i in range (0, len(tt)):
            print(tt[i])
        return
    else:
        print("input was not a Tuple, but rather of type: " + str(type(tt)) + "\nand had a value of: "+ str(tt))
        return

#extra solution 1
    # for item in tt:
    #     print(item)
#extra solution 2
    # if iter(tt):
    #     for i in range (0, len(tt)):
    #         print(tt[i])
    #     return
    # else:
    #     print(tt)
    #     return
#extra solution 3
    # try:
    #     for i in range (0, len(tt)):
    #             print(tt[i])
    #         # return
    # except TypeError:
    #     print("not a tuple, but it's: " + str(tt))

t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
u = (1)  # What needs to be added to make this work?
#I'm not 100% sure what is being asked here, but I added some solutions and left my favorite uncommented out.
#some of the commented out solutions may not be 100% working
print_tuple(u)


print_tuple("lmao")

print_tuple([1,2,3])