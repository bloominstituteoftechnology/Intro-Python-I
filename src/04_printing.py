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
name = "John"
print("Hello, %s!" % name)

# # 2. To use two or more argument specifiers, use a tuple (parentheses)
 # This prints out "John is 23 years old."
name = "John"
age = 23
print("x is %d, y is %f, z is %s." % (x, y, z))

print("The %d turtles eat %f pounds of food daily.%s." % (x, y, z))

# Use the 'format' string method to print the same thing

# Finally, print the same thing using an f-string

#>>> first_name = "Eric"
#>>> last_name = "Idle"
#>>> age = 74
#>>> profession = "comedian"
#>>> affiliation = "Monty Python"
#>>> "Hello, %s %s. You are %s. You are a %s. You were a member of %s." % (first_name, last_name, age, profession, affiliation)
#Workin'Hello, Eric Idle. You are 74. You are a comedian. You were a member of Monty Python.'