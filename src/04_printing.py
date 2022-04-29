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

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

# 4
# https://github.com/LambdaSchool/Intro-Python-I/blob/master/src/04_printing.py

# see: https://stackoverflow.com/questions/5082452/string-formatting-vs-format

x = 10
y = 2.24552
z = "I like turtles!"

# not so clear: https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html
# Using the printf operator (%), print the following feeding in the values of x, y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %(x)d, y is %(y)1.5f, z is "%(z)s"' % {"x": 10, "y": 2.24552, "z": "I like turtles!"})

# https://www.programiz.com/python-programming/methods/string/format
# Use the 'format' string method to print the same thing
# default arguments
print('x is {}, y is {}, z is "{}"'.format(10, 2.24552, "I like turtles!"))

# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, z is "{z}"')