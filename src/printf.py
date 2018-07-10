x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"


# Use the 'format' string method to print the same thing

print('x is %i, y is %.2f, z is %s' % (x , y, z))

print('x is %(x)i, y is %(y).2f, z is %(z)s' % {'x':x, 'y':y, 'z':z})



print(f'x is {x}, y is {y}, z is {z}, y is super {y:.2f} ')

print('x is {}, y is {:.2f}, z is {}'.format(x,y,z))

print('x is {0}, y is {1:.2f}, z is {2}, and Derrick says {2}'.format(x,y,z))
