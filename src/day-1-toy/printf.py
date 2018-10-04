x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %0.2f, z is "%s"' % (x, y, z)) # %04d means there will be four numbers 0010 with 0 filling any missing numbers.  
                                                      # %0.2 means there will be a decimal two points past the dot

# Use the 'format' string method to print the same thing
print('x is {0:d}, y is {1:0.2f}, z is "{2:s}"'.format(x, y, z))