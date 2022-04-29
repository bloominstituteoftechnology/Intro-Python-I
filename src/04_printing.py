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

#sal example
# name = "John"
# age = 23
# print("%s is %d years old." % (name, age))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# print(f"{x is: x}, {y is: y}, z is z")
print("x is %d, y is %f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing
# >>> print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))
# 6 bananas cost $1.74

print('x is {0}, y is {1}, z is {2}'.format(10, 2.25,'I like Turtles!'))

# Finally, print the same thing using an f-string

# >>> quantity = 6
# >>> item = 'bananas'
# >>> price = 1.74
# >>> print(f'{quantity} {item} cost ${price}')
# 6 bananas cost $1.74

print(f'x is {x}, y is {y}, z is {z}')

