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
# f - is for 'fixed number" -- .2(fix the number to two places after the decimal)
print("x is %i, y is %.2f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing
# index position must be used when using other arguments, in this case for the second (1) position
###I am fixing to two decimal places
str = "x is {0}, y is {1:.2f}, z is {2}"
print(str.format(x,y,z))

# Finally, print the same thing using an f-string
### for fixed decimal, use the key value instead of the index value as per above
print(f"x is {x}, y is {y:.2f}, z is {z}")