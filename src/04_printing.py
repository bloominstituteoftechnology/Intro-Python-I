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
# attempt one
x = 10
y = round(2.24552, 2)
z = "I like turtles!"
print('%d %d %s' % (x, y, z) )
# attempt two
data = (10, 2.25, "I like turtles")
format_string = '%d %d %s'
print(format_string % data)

# Use the 'format' string method to print the same thing
data = {'x': 10, 'y': 2.25, 'z': 'I like turtles!'}
print("{x} {y} {z}".format(x=data['x'], y=data['y'], z=data['z']))


# Finally, print the same thing using an f-string
x = 10
y = round(2.24552,2)
z = "I like turtles!"
print(f'{x} {y} {z}')
