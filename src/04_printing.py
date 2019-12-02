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
str.format() is one of the string formatting methods in Python3, which allows multiple substitutions and value formatting. 
This method lets us concatenate elements within a string through positional formatting.

Using a Single Formatter :
Formatters work by putting in one or more replacement fields and placeholders defined by a pair of curly braces { } into a string and calling the str.format(). 
The value we wish to put into the placeholders and concatenate with the string passed as parameters into the format function.


PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal). 
The idea behind f-strings is to make string interpolation simpler.

To create an f-string, prefix the string with the letter f . 
The string itself can be formatted in much the same way that you would with str.format(). 
F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

f-strings are string literals that have an f at the beginning and curly braces containing expressions that will be replaced with their values.

like template literal(?'s)


{:d} => It is a formatting character.
It tells the formatter to treat the argument as an integer number and format it as such. 
Other valid formatters could be x to format it as a hexadecimal number, or b for binary, etc.
"""

# Use the 'format' string method to print the same thing
print('FORMAT STRING 1', format(z))
print('FORMAT STRING 2', '{:d}'.format(x))
print('FORMAT STRING 3', '{:f}'.format(y))

# Finally, print the same thing using an f-string
print(f'{z}')
print(f'{x} is an integer and {y} is a float')

#could also do something like this 
random = ( 
    f'{z}' 
    f'{x}' 
    f'{y}'
)
print(random)