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

print("My favorite number is %s, but my second favorite is %s, and also, %s" % (x, y, z))

# Use the 'format' string method to print the same thing

print("My favorite number is " + str(x) + ", but my second favorite is " + str(y) + ", and also, " + z)


# Finally, print the same thing using an f-string

print(f"My favorite number is {x}, but my second favorite is {y}, and also, {z}")
