x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("My son is %d years old and my daughter is %f! And I %s" % (x, y, z))

# Use the 'format' string method to print the same thing
print("My son is {} years old and my daughter is {}! And I {}".format(x, y, z))

# Use the new f string format to print out the same thing. Amazing I got it to work!
print(f"My son is {x:i} years old and my daughter is {y} ! And I {z:f}")
