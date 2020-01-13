"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.

https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html - old (%)
https://pyformat.info/ - new (.format())
https://realpython.com/python-f-strings/ - f-strings
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %(x)i, y is %(y)g, z is %(z)r' % {"x":x, "z":z, "y":y})

# Use the 'format' string method to print the same thing
print('x is {0}, y is {2}, z is {1!r}'.format(x, z, y))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, z is '{z}'")