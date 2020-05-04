"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.

To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
info = 'x is %i, y is %f, and z is %s'
values = x, y, z
print(info % values)

# Use the 'format' string method to print the same thing
sentence = "x is {}, y is {}, and z is {}".format(x, y, z)
print(sentence)
# Finally, print the same thing using an f-string
print(f'x is {x}, y is {y}, and z is {z}')