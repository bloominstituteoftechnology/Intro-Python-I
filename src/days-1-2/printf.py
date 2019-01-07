x = 10
y = 2.24552
z = "I like turtles!"
group = (x, y, z)
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %s, y is %s and z is %s" %(x,y,z))
# Use the 'format' string method to print the same thing
print('x is {0[0]}, y is {0[1]} and z is {0[2]}'.format(group))
# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y} and z is {z}.")