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
print("\nUsing the printf operator (%)")
print("\nx : %d, y : %f, z : %s" % (x, y, z))

# Use the 'format' string method to print the same thing
print("\nUsing the 'format' string method")
print("\nx : {0}, y : {1}, z : {2}".format(x, y, z))

# Finally, print the same thing using an f-string
print("\nUsing an f-string")
print(f"\nx : {x}, y : {y}, z : {z}")