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
print ("%i %f %s" %(x, y, z))

# %d or %i = integer
# %f = float
# %s = string

# Use the 'format' string method to print the same thing
print (("{} is x").format(x))
print(("{} is y").format(y))
print(("{} is z").format(z))

print(("{}, {}, {}").format(x,y,z))

# Finally, print the same thing using an f-string

print(f"X is, {x}. Y is {y}. Z is {x}") #lower case
print(F"X is, {x}. Y is {y}. Z is {x}") #upper case