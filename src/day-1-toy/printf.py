x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('X is %d, Y is %.2f, Z is "%s"' % (x, y, z))


# Use the 'format' string method to print the same thing
sent = f"X is {x}, Y is {y}, Z is {z}"

print(sent)
