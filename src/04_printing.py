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
print("Using printf")
print("x is %2d, y is %3.2f, z is \"%s\"" % (x, y, z))
# Use the 'format' string method to print the same thing
print("Using format")
string = "x is {}, y is {}, z is \"{}\"".format(x, round(y, 2), z)
print(string)
# Finally, print the same thing using an f-string
print("Using f-string")
print(F"x is {x}, y is {round(y, 2)}, z is \"{z}\"") 