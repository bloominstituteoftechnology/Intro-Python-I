x = 10
y = 2.24552
z = "I like turtles!"

#unfinished
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
text = ('x is %i, y is %.2f, z is "%s"' %(x, y, z))
print(text)

# Use the 'format' string method to print the same thing
print ('x is {}, y is {:.2f}, z is "{}"'.format(x, y, z))

# Finally, print the same thing using an f-string
f'x is {x}, y is {y}, z is "{z}"'
