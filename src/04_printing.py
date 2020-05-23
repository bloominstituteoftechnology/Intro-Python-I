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
y = round(y, 2)
print(y)

print('%d is 10, %s is 2.25, %s is "I like turtles!"' % (x, y, z))

# Use the 'format' string method to print the same thing
str = '{} is 10, {} is 2.25, {} is "I like turtles!"'
print(str.format(x, y, z))

# Finally, print the same thing using an f-string
print(f"x is", x)
print(f"y is {y}")
print(f"z is {z!r}")

# f-strings not working even though my python version should be good enough.