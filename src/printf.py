x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# print('%x is', x, '%y is', y, '%z is', z)
print('y is %f, and z is %s' %(y, z))
# Use the 'format' string method to print the same thing
# print('x is', x, 'y is', y, 'z is', z)
string_concat = 'x is, ' + str(x) +' and y is ' + str(y) + ' z is ' + z
# print(string_concat)
print('x is {}, y is {}, z is {}'.format(x, y, z))