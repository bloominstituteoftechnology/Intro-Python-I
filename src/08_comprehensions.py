"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated.

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [item for item in range(1, 6)]
print(y)

# write a list comprehension to produce the cubes of the numbers 0-9
# should output [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [item**3 for item in range(0, 10)]
print(y)

# write a list comprehension to produce the uppercase version of all the elements in array a
# hint: 'foo'.upper() is 'FOO'

a = ['foo', 'bar', 'baz']
y = [item.upper() for item in a]
print(y)

# use a list comprehension to create a list containing only the even elements the user entered into list x
# what do you need between the square brackets to make it work?

x = input('enter comma-separated numbers: ').split(',')
print(x)
y = [int(item) for item in x if int(item) % 2 == 0]
print(y)