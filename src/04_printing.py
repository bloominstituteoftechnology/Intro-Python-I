"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
"""
'%' initiates the string interpolation 
2 signifies (2 spaces), d means singed integer decimal
4 signifies (4 spaces), .2 means how many digits following the decimal, f means floating number
2 signifies (2 spaces), s stands for type string
"""

print('x is %2d, y is %4.2f, z is %2s' % (x, y, z))

# Use the 'format' string method to print the same thing
print('x is {0:2d}, y is {1:4.2f}, z is {2:2s}'.format(x, y, z))

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y:4.2f}, z is {z}')
