x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print(f"x is {x}, y is {y}, z is \"{z}\"")

# Use the 'format' string method to print the same thing
print("x is {x}, y is {y}, z is '{z}'".format(x=10, y=2.24552, z="I like turtles!"))

# Use the printf operator and the 'format' string method and see what happens
print(f"x is {x}, y is {y}, z is \"{z}\"".format(x=10, y=2.24552, z="I like turtles!"))
