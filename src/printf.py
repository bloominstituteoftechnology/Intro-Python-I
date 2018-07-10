x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# '%d %d %s' % (x, y, z)
print('%d %04.2f %s' % (x, y, z))

# Use the 'format' string method to print the same thing
print('{} {:04.2f} {}'.format(x, y, z))
