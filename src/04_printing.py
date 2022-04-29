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
print("x is %d, y is %f, z is %s"%(x, y, z))
print()

# Use the 'format' string method to print the same thing

txt = "x is {x1:d}, y is {y1:f}, z is {z1:s}"
print(txt.format(x1 = x, y1 = y, z1 = z))
print()

txt2 = "x is {x1:d}, y is {y1:f}, z is {z1:s}".format(x1 = x, y1 = y, z1 = z)
print(txt2)
print()

print("x is {x1:d}, y is {y1:f}, z is {z1:s}".format(x1 = x, y1 = y, z1 = z))
print()



# Finally, print the same thing using an f-string

print(f"x is {x}, y is {y}, z is {z}")