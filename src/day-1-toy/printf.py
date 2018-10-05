x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("integer: %d" % (x))
print("%.3f" % (y)) #.3 or .2 .5 for the number of decimals to be included with float
print("string: %s" % (z))

# Use the 'format' string method to print the same thing

print('x is {0}, y is {1}, z is {2}'.format(x, y, z))
# Is the same as:
print('x is {}, y is {}, z is {}'.format(x, y, z))
# auto numbering when they are empty, in the order of .format([0],[1],[2] ...)

print('x is {}, y is {:.2f}, z is {}'.format(x, y, z))
# seems that .2f is considered automatic numbering, so the other curlies have to be auto too
print('x is {2}, y is {1:.2f}, z is {0}'.format(x, y, z))
# this works with assigning a number in front of the colon on the float to manually assign the order

# print(f'x is {x}, y is {y}, z is {z}')