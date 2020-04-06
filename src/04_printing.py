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
print("y = %1.5f, x = %d, %s"% (y, x, z))
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing
print("y = {}, x = {}, {}".format(y, x, z))

# Finally, print the same thing using an f-string
print(f"y = {y}, x = {x}, {z}")