"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of
# x, y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print(" %d " % x)
print(" %f " % y)
print(" %s " % z)

# https://docs.python.org/3/library/stdtypes.html#old-string-formatting

# Use the 'format' string method to print the same thing
print('{x}, {y}, {z}'.format(x=x, y=y, z=z))
print('{}'.format(x))
print('{}'.format(y))
print('{}'.format(z))

# https://realpython.com/python-string-formatting/

# Finally, print the same thing using an f-string
print(f'{x}')
print(f'{y}')
print(f'{z}')
