x = 10
y = 213123212.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

print ("x is %s, y is %1.2f, z is %s" % (x,y,z))

print ("x is {}, y is {:3.2f}, z is {}".format(x,y,z))

print (f"x is {x}, y is {y:3.2f}, z is {z}")