x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print('x is %d, y is %1.2f, z is %s'%(x, y, z))

# print(f'x is {x:.3f}, y is {y}, z is {z}')

# Use the 'format' string method to print the same thing
print('x is {0}, y is {1:.3}, z is {2}'.format(x, y, z)) 



# print("x is",x, ", y is",y, ", z is",z)   <- Was just messing around with this one, it's not required