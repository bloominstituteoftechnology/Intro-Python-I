"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
# [y.append(x+1) for x in range(5)]
y = [x + 1 for x in range(5)]

# for x in range(5):
#     y.append(x+1)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# y = []
# [y.append(x**3) for x in range(10)]
y = [cubes**3 for cubes in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []
# [y.append(x.upper()) for x in a]
y = [word.upper() for word in a ]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [i for i in x if int(i) % 2 == 0]

# y = [num for num in x if int(num) % 2 == 0]
# y = [int(num) for num in x if int(num) % 2 == 0]

print(y)

a_list = [1, 2, 3, 4, 5, 6]

list_copy = [x for x in a_list]

for x in a_list: 
    x

odds = [x for x in a_list if x % 2 == 1]
for x in a_list:
    if x % 2 == 1: 
        x

list_of_strings = ["hello", "world", 1, 2]

f'my string and my list comprehension: {[x for x in list_of_strings if type(x) == str]}'

just_strings = [x for x in list_of_strings if type(x) == str] 
for x in list_of_strings:
    if type(x) == str:
        x