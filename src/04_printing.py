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
"""
Considered "Old Style" String Formatting (% Operator)
using the %s format secifier tells Python where to subsititue the value of
name, represented as a string.
"""

print('Print Operator %:')
print('x is% 2d, y is% 2.2f, z is "% s"' % (x, y, z), '\n')

"""
Considered "New Style" String Formatting (str.format) which is a new way to do
string formatting. This string formatting gets rid of the %-operator special
syntax and makes the syntax for string formatting regular.
"""
print('+-----------------------------------------+')
# Use the 'format' string method to print the same thing
print('Format String Method:')
print('x is {0}, y is {1:.2f}, z is "{2}"'.format(x, y, z), '\n')

"""
String Interpolation / f-Strings
Also a new way of formatting strings which lets you use embedded Python
expression inside string constants.
"""

print('+-----------------------------------------+')
# Finally, print the same thing using an f-string
print('F-String:')
print(f'x is {x}, y is {round(y, 2)}, z is "{z}"', '\n')
