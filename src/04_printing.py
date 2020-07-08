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
print("Method 1.a, C-style printf: x is %d, y is %.2f, z is %s" % (x, y, z))
print("Method 1.b, C-style printf: x is %(x)d, y is %(y).2f, z is %(z)s" % {"x": x, "y": y, "z": z})

# Use the 'format' string method to print the same thing
print("Method 2, format(): x is {x}, y is {y:.2f}, z is {z}".format(x = x, y = y, z = z))


# Finally, print the same thing using an f-string:
print(f"Method 3, f-string: x is {x}, y os {y:.2f}, z is {z}")
