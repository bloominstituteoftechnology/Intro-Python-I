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
print("x = % 2d" % (10))
print("y = % 3.2f" % (2.24552))
print("z = % s" % ('I like turtles!'))

# Use the 'format' string method to print the same thing
print('x = {0}'.format(10))
print('y = {0:3.3}'.format(2.24552))
print('z = {0}'.format('I like turtles!'))

# Finally, print the same thing using an f-string
print(f'x = {x}')
print(f'y = {y:3.2f}')
print(f'z = {z}')
