"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [e for e in range(1,6)]

print(y)



# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [e**3 for e in range(0,10)]


print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [element.capitalize() for element in a ]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = [3,5,6,7,9,10]


# What do you need between the square brackets to make it work?
y=[e for e in x if e%2 == 0]


print(y)