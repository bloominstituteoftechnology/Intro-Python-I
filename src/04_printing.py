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
<<<<<<< HEAD
print("x is %s, y is %f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing
print("x is {x}, y is {y}, z is {z}".format(x = x, y = y, z = z))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, z is {z}")
=======
print(f"{x} is 10, {y} is 2.25, {z}")

# Use the 'format' string method to print the same thing
print("{0} is 10, {1} is 2.25, {2}".format(x, y, z))

# Finally, print the same thing using an f-string
print (f"{x} is 10, {y} is 2.25, {z}")
>>>>>>> 32ce47e229be817cd10ac238ffaf4e24c29a1f9f
