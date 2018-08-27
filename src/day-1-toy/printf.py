x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %d, y is %.2f, z is \"%s\"" % (x, y, z))


# Use the 'format' string method to print the same thing
# print("x is %2i, y is %1.2f, z is %s" % (x, y, z))
print("x is {}, y is {:.2f}, z is \"{}\"".format(x, y, z))

#https://www.python-course.eu/python3_formatted_output.php