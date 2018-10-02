x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("integer: %d" % (x))
print("float: %f" % (y))
print("string: %s" % (z))

# Use the 'format' string method to print the same thing

print('x is {0}, y is {1}, z is {2}'.format(x, y, z))