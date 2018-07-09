x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# Refer to https://pyformat.info/ for more info
print('x is %i, y is %.*f, z is "%s"' % (x, 2, round(y, 2), z))
# Arguments passed after `%` is `x`, precision (`2`), `y` rounded to 2 places, `z`

# Use the 'format' string method to print the same thing
print('x is {}, y is {}, z is "{}"'.format(x, round(y, 2), z))

# Formatted String Literals
print(f'x is {x}, y is {round(y, 2)}, z is "{z}"')