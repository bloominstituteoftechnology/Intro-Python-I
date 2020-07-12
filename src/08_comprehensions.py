"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(1, 6)]

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
cubes = [i**3 for i in numbers]
print(cubes)

#
# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".
#
words = ["foo", "bar", "baz"]

uppercase = [w.upper() for w in words]

print(uppercase)

# Use a list comprehension to create a list containing only even
# the user entered into list x.
#
x = input("Enter comma-separated numbers: ").split(',')
for i in range(0, len(x)):
    x[i] = int(x[i])

evens = [i for i in x if i % 2 == 0]
print(evens)
# What do you need between the square brackets to make it work?
