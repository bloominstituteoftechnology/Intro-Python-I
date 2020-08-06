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

print("x is %5d, y is %8.2f z is %r" % (x, y, z))
# round(number, # of decimal places) used to get it to match the input above
# Use the 'format' string method to print the same thing
s = "x is {x}, y is {y}, z is '{z}'".format(x=x, y=round(y, 2), z=z)
print(s)

# Finally, print the same thing using an f-string

print(f"x is {x}, y is {round(y,2)}, z is '{z}'")
