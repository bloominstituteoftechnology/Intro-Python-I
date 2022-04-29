"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('x is %d, y is %1.2f, z is "%s"' %(x, y, z))

# Use the 'format' string method to print the same thing
formatmethodstring = ('x is {0}, y is {1:1.2f}, z is "{2}"'.format (x, y, z))
print(formatmethodstring)

# Finally, print the same thing using an f-string
f"x is {x}, y is  {y}, z is {z}"


# # This prints out "Hello, John!"
# name = "John"
# print("Hello, %s!" % name)

# # 2. to use two or more argument specifiers

# age = 23
# print("%s is %d years old." %(name, age))

# # 3. any object that is NOT a string can be formatted using %s
# # %d - integers
# # %f - floating point numbers
# # %.<number of digits> - floating point numbers
# # wtha fixed amount of digit to the right of the dot.

# # this prints out: A list: [1, 2, 3]
# mylist = [1,2,3]
# print("A list: %s" % mylist)

# #  index of first instance
# astring = "Hello, World"
# print(astring.index("l"))

# # count of variable
# print(astring.count("l"))

# # slice of a string, starting an ending at different index
# print(astring[3:7])

# # [start:stop:step]
# print(astring[3:7:2])

# # reverse a string
# print(astring[::-1])

# # upper and lower
# print(astring.lower())
# print(astring.upper())

# # startswith and endswith which return booleans
# print(astring.startswith("Hello")) # true
# print(astring.endswith("asdfasdf")) # false

# split
# afewwords = astring.split(" ")
# print(afewwords)











