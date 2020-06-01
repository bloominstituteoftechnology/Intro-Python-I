"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

y_rounded = ("%f" % round(y, 2))
y_shortened = y_rounded.rstrip('0')
# testing that y is converted from 2.24552 to 2.25
print("THIS IS A TEST " + str(y_shortened))

# Question 1
# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

# Tip: You have to keep track of the order of the variables and match the format symbol with the set after the sentence
sentence = "1) x is %s, y is %s, z is %s" % (x, y_shortened, z)
print(sentence)
# option 2:
# print("1) x is %s, y is %s, z is %s" % (x, y, z))

#################################

# Question 2
# Use the 'format' string method to print the same thing

sentence = "2) x is {}, y is {}, z is {}".format(x, y_shortened, z)
print(sentence)
# option 2:
# print("x is {}, y is {}, z is {}".format(x, y, z))

#################################

# Question 3
# Finally, print the same thing using an f-string

# Tip: You just enter an empty object and can further format within the object if needed. ex: {z.upper()} instead of just {} to make that variable uppercase
# the youtube video boy actually screams this. this is the only correct answer.
sentence = f"3) x is {x}, y is {y_shortened}, z is {z.upper()}"
print(sentence)
# option 2:
# print(f"x is {x}, y is {y}, z is {z}")
