"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [x for x in range(1,6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cubes = [pow(x,3) for x in range(10)]

print(cubes)

# Write a list comprehension that utilizes slicing syntax to product 
# a list with the elements from the first half of the `cubes` list

first_half_of_cubes = cubes[0:int(len(cubes)/2)]

print(first_half_of_cubes)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

lowercase = ["foo", "bar", "baz"]

uppercase = [x.upper() for x in lowercase]

print(uppercase)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [number for number in x if int(number) % 2 == 0]

print(y)