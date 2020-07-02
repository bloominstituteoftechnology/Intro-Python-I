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
print("printf","x is %2d, y is %7.5f, z is %s" % (x, y, z))
# Use the 'format' string method to print the same thing
statement = "x is {}, y is {}, z is {}".format(x, y, z)
print("format string method", statement)
# Finally, print the same thing using an f-string
sentence = f'x is {x}, y is {y}, z is {z}'
print("f string", sentence)
#the f string is by far the most intuitive of these 
# printf seems like a nightmare to deal with
