x = 10
y = 2.24552
z = 'I like turtles!'

# using the printf operator (%), print the following feeding in the values of x, y, and z

# x is 10, y is 2.24552, z is 'I like turtles!'

print("x is %d, y is %f, z is '%s'" %(x, y, z))

# use the 'format' string method to print the same thing

print("x is {}, y is {}, z is '{}'".format(x, y, z))

# finally, print the same thing using an f-string

print(f"x is {x}, y is {y}, z is '{z}'")