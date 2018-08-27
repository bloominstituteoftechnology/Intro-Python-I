x = 10
y = 12.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %i, y is %f, z is %s' % (x, y, z))

# Use the 'format' string method to print the same thing
print('x is {}, y is {}, z is {}'.format(x, y, z))
print('x is {0}, y is {1:.3}, z is "{2}"'.format(x, y, z))
