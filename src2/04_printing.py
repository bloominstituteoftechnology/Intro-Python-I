import os

"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# print(z)
print(z) 
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

print()
print("Brian")
print()
print("Good evening")
print()
print("BMW 3 Series \nBMW 5 series".rstrip()) #with rstip()
print()

print("Brian \nVilchez") 
print("Currently learning python for computer science.")

message = "Hello there welcome to python!"
print(message)
print(f"Hello there { os.getlogin() }")

long_message = "This is a very long message, that needs to be broken down to multiple lines."
print(long_message, sep=',')