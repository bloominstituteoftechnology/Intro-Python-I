# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE

import math

""" Note that this did not work:
power = math.pow(2, 65536)

However, this does:
power = 2 ** 65536

The problem is that math.pow(..) works on floating point numbers. 
In Python floating point numbers are not arbitrary large. Only ints are (in python-3.x, and longs in python-2.x).

You can however use the ** operator which does integer power
 (given of course the arguments are integers) if the two numbers are integers:

"""

power = 2 ** 65536
print (power)