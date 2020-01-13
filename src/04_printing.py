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

print('Will it work let us see, %s ' % z)
print('Okay here is one number, %f ' % y)
print('And the other: %i ' % x)

# Use the 'format' string method to print the same thing
print(z.format())
str_y = str(y)
print(str_y.format())
str_x = str(x)
print(str_x.format())

# Finally, print the same thing using an f-string