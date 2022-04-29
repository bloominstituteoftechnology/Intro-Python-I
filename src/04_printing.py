"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# x is 10, y is 2.25, z is "I like turtles!"
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
print("x is %d, y is %.2f and z is %s"%(x, y, z))

# Use the 'format' string method to print the same thing
text = "x is {x}, y is {y}, z is {z}".format(x = 10, y = 2.25, z = "I like turtles!")
print(text)

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, z is {z}")
