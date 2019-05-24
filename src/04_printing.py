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
print('X is %d, Y is %.2f, Z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
print('X is {0:d}, Y is {1:.2f}, Z is "{2:s}"'.format(x, y, z))

# Finally, print the same thing using an f-string
print(f'X is {x:d}, Y is {y:.2f}, Z is "{z:s}"')
