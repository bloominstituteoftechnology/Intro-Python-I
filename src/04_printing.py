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

print('%2d %2.5f ' %(x, y) + z)

# Use the 'format' string method to print the same thing

txt1 = z + " {} {} ".format(x,y)
txt2 = " {} {} ".format(x,y) + z
print(txt2)

# Finally, print the same thing using an f-string

print(f" {x} {y} "+z)