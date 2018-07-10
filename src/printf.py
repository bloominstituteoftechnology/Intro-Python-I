x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is %2d, y is %2.5f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing

formatString = 'x is {}, y is {}, z is "{}"'

print(formatString.format(x, y, z))