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
'%.2f' % y shows 2 decimals
"""
print('x is', x, ', y is', '%.2f' % y, ', z is', '"'+z+'"')

# Use the 'format' string method to print the same thing
"""
"{0:.2f}".format(y) shows 2 decimals
"""
print('x is', x, ', y is', "{0:.2f}".format(y), ', z is', '"'+z+'"')


# Finally, print the same thing using an f-string
"""
{} show the values in the same order that are defined in
.format()
"""
print(f'x is {x}, y is {"{0:.2f}".format(y)}, z is "{z}"')
# or print('x is {} ,y is {} ,z is "{}"'.format(x, "{0:.2f}".format(y), z))