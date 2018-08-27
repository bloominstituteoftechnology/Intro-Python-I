x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %(firstNum)s, y is %(secondNum)s, z is "%(sentence)s"' % {"firstNum":x, "secondNum":y, "sentence": z})

# Use the 'format' string method to print the same thing
print('x is {}, y is {}, z is "{}"'.format(x, y, z))
print('x is {0}, y is {1}, z is "{2}"'.format(x, y, z))
