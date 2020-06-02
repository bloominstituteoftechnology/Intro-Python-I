"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
import sys


def printf(format, *args):
    sys.stdout.write(format % args)


x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

printf(" xi is %d, y is %d, z is %s", x, y, z)

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string
