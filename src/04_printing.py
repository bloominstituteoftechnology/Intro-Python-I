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
z = "I like turtles!"
print("x is %2d, y is %3.2f, z is %s " %(10, 2.25, z))

# Use the 'format' string method to print the same thing
txt = "x is {int:2d}, y is {float:3.2f}, z is {ss:s}"
print(txt.format(int = 10, float = 2.25, ss = "I like turtles!"))

# Finally, print the same thing using an f-string

f"x is {x} y is {y}, z is {z}"