"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""
x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%),
# print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
format_1 = 'x is %d, y is %2.2f, z is "%s"' % (x, y, z)
print(format_1)
print()

# Use the 'format' string method to print the same thing
format_2 = 'x is {}'.format(x)
+ ', y is {:.2f}'.format(y) + ', z is "{}"'.format(z)
print(format_2)
print()

# Finally, print the same thing using an f-string
format_3 = f'x is {x}, y is {y:.{2}f}, z is "{z}"'
print(format_3)
print()
