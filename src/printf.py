x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# print('%d %04.2f %s' % (x, y, z))
print('%d %.2f %s' % (x, y, z))

# Use the 'format' string method to print the same thing
# print('{} {:04.2f} {}'.format(x, y, z))
print('z is {2}, y is {1:.2f}, x is {0}'.format(x, y, z))

print (f'x is {x}, y is {y} , z is {z}')
