x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
printf('x is %d, y is %.2f, z is %s %(10,2.24552, "I like turtles!")')

# Use the 'format' string method to print the same thing

format_string=" x is {}, y is {}, z is {}"
print(format_string.format("10","2.24552","I like turtles!"))