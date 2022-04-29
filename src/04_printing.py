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
print ("%s is 10, %s is 2.25, %s is I like turtles!" % (x, y,z))



# Use the 'format' string method to print the same thing
strings = "{one} is 10, {two} is 2.25, {three} is I like turtles!"
print(strings.format(one = x, two = y, three = z))
# Finally, print the same thing using an f-string
# ####
print(f"{x} is 10, {y} is 2.25, {z} is I like turtles!")