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
string1 = ('x is %i, y is %f, z is %s' %(x, y, z))
print(string1)
# note that %i is for integer, %f is for float, %s is for string

# Use the 'format' string method to print the same thing
string2 = ('x is {}, y is {}, z is {}'.format(x, y, z))
print(string2)

# Finally, print the same thing using an f-string
string3 = f'x is {x}, y is {y}, z is {z}'
print(string3)