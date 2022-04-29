"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

print("\nWrite a list comprehension to produce the array [1, 2, 3, 4, 5]")

y = []
y = [x + 1 for x in range(5)]

print (y)

print("\nWrite a list comprehension to produce the cubes of the numbers 0-9:")
print("\n[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]")

y = [x**3 for x in range(10)]

print(y)

print("\nWrite a list comprehension to produce the uppercase version of all the")
print("\nelements in array a. Hint: 'foo'.upper() is 'FOO'.")

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]

print(y)

print("\nUse a list comprehension to create a list containing only the _even_ elements")
print("the user entered into list x.\n")

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [i for i in x if (int(i) % 2) == 0]

print(y)