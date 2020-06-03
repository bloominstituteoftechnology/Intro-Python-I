"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.25
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %2d, y is%5.2f, z is %3s" %(10,2.25, "I like turtles!"))
# Use the 'format' string method to print the same thing
print("x is {}, y is {}, z is {}".format(10,2.25, "I like turtles!"))
# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, z is {z}")


# def stupid_addition(a,b) :
#     if type(a) == str and type(b) == str:
#         return (int(a) + int(b))
#      if type(a) == int and type(b) == int:
#          return (str(a) + str(b))

# stupid_addition("1","2")