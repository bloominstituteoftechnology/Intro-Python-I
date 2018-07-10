x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("""
% :
x = %d
y = %.2f
z = %s
""" % (x, y, z))

# Use the 'format' string method to print the same thing
print("""
.format():
x = {2}
y = {1}
z = {0}
""".format(z, y, x))

print(f'x is {x}, y is {y}, z is {z} ')
