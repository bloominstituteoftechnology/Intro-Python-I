x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %d, y is %.2f, z is %s" % (x, y, z))
a = 1
b = 3
# Use the 'format' string method to print the same thing
print(f"x is {x!r} y is {y:{a}.{b}}, z is {z!s}")

str = "x is {} y is {:.2f} z is \"{}\""
print(str.format(x, y, z))