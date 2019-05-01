"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

## %s - String (or any object with a string representation, like numbers)
## %d - Integers
## %f - Floating point numbers

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
rounded_y = round(y, 2)
print("x is %s, y is %s, z is \"%s\"" % (x, rounded_y, z))

# OR round the number in the string formatting

print('x is %d, y is %.2f, z is "%s"' % (x, y, z))

# Use the 'format' string method to print the same thing
print("x is {0}, y is {1}, z is \"{2}\"".format(x, rounded_y, z))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {rounded_y}, z is \"{z}\"")