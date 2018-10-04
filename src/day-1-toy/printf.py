x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# print("x is %s, y is %s, z is %s "%(x, y, z))
# print('x is {x}, y is {y}, z is "{z}"'.format(x = 10, y=2.24552, z="I like turtles!"))

print('x is {0}, y is {1:.2f}, z is "{2}"'.format(x, y, z))

# Use the 'format' string method to print the same thing
print(f'x is {x}, y is {y:.2f}, z is "{z}"')

