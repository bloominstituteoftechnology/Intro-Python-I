"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"
# # print integer and float value
# print("Geeks : % 2d, Portal : % 5.2f" %(1, 05.333))

# # print integer value
# print("Total students : % 3d, Boys : % 2d" %(240, 120))

# # print octal value
# print("% 7.3o"% (25))

# # print exponential value
# print("% 10.3E"% (356.08977))
# Output :

# Geeks :  1, Portal : 5.33
# Total students : 240, Boys : 120
# 031
# 3.561E+02
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("X is % 2d, Y is % 2.2f, Z is % s" %(x,y,z))

# Use the 'format' string method to print the same thing
print("X is {}, Y is {}, Z is {}".format(x,y,z))
# Finally, print the same thing using an f-string
f"x is {x}, y is {y}, z is {z}"
