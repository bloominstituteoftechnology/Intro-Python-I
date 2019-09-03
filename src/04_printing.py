"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %.2f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
print('x is {}, y is {:.2f}, z is {!r}'.format(10, 2.224552, "I like turtles!"))

# Finally, print the same thing using an f-string
# This print has invalid syntax, figure it out later
print('x is {x}, y is {y}, z is "{z}"')
