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
print('printf operator (%)')
print('x is %s, y is %s, z is "%s"' % (x, y, z))
print("\n")

# Use the 'format' string method to print the same thing
print("'format' string method")
print('x is {}, y is {}, z is "{}"'.format(x, y, z))
print("\n")

# Finally, print the same thing using an f-string
print("f-string")
print(f'x is {x}, y is {y}, z is "{z}"')
print("\n")
