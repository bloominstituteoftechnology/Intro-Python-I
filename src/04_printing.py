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
stringFormat1 = 'x is %s y is %.2f  and z is %s' % (x, y, z)
print(stringFormat1)
# Use the 'format' string method to print the same thing
stringFormat2 = 'x is {x} y is {y: .2f}  and z is {z}'.format(x=x, y=y, z=z)
print(stringFormat2)
# Finally, print the same thing using an f-string
stringFormat3 = f'x is {x} y is {y: .2f}  and z is {z}'
print(stringFormat3)
