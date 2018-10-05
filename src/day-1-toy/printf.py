x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print ('x is %s, y is %s, z is %r' %(x, round(y,2), z))

# Use the 'format' string method to print the same thing
print ("x is {!s}, y is {!s}, z is {!r}".format(x, round(y,2), z))

print (f"x is {x}, y is {round(y,2)}, z is '{z}'")

