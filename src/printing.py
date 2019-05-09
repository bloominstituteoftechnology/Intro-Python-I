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

print('x is %s!' % x)
print('y is %s!' % y)
print('z is %s' % z)

# Use the 'format' string method to print the same thing

str = "x is {}"
print (str.format(x)) 

str = "y is {}"
print (str.format(y)) 

str = "z is {}"
print (str.format(z)) 

# Finally, print the same thing using an f-string

# name = "Eric"
# >>> age = 74
# >>> f"Hello, {name}. You are {age}."
# 'Hello, Eric. You are 74.'

print (f'x is {x}')

print (f'y is {y}')

print (f'z is {z}')