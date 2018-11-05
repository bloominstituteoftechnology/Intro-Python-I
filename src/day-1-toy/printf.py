x = 10
y = 2.24552
z = "I like turtles!"


# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %d, y is %.2f, z is \"%s\"" % (x, y, z))

# Use the 'format' string method to print the same thing
print("x is {}, y is {:.2f}, z is \"{}\"".format(x, y, z))
# Finally, print the same thing using an f-string
# “formatted string literals,” f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values. The expressions are evaluated at runtime and then formatted using the __format__ protocol
f"{x}, {y}, {z}"
