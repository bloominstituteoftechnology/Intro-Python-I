"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
array_5=[n+1 for n in range(5)]

print(array_5)



# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [n**3 for n in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [n.upper() for n in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
#y = [n%2==0 for n in x]

#n comes first because we arent changing the inputs
#'n for n in x'
#'if' filters the list by the condition set after it
# 'n%2==0` is the condition, will only show those that meet condition
#the only place we need it to be a number is when we're doing math

yy = [n for n in x if int(n)%2==0]

print(yy)