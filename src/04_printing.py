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
print("%f, and %s" %(y, z))
print("x is %d, y is %f, and z is %s" %(x,y,z))

# Use the 'format' string method to print the same thing
print("{}, and {}".format(y,z))
print("x is {}, y is {}, and z is {}".format(x,y,z))
# Finally, print the same thing using an f-string
print(f"{y} and {z}")
print(f"{x} is 10, y is {y} and z is {z}")
