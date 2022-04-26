"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = round(2.24552, 2)
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %i, y is %f.2, z is %s' % (10, 2.24552, 'I like turtles!'))

# Use the 'format' string method to print the same thing
text = "x is {0}, y is {1}, z is {2}".format(
   10, round(2.24552, 2), "I like turtles!")
print(text)
# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is {z}')


