x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"


# Use the 'format' string method to print the same thing

print('x is %(x)i , y is %(y)1f , and z is %(z)s' %
{"x": 10, "y" : 2.25, "z": "I like turtles!"})

#print '{} {} {}'.format(x,y,z)