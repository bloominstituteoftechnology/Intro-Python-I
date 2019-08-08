# Notes:
# #Can make lists from expressions (listcomprehension)
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 4, 9, 25]
# square = []
# # for num in numbers:
#   # quares.append(num*num)
# squares = [num*num for num in numbers]
# print(numbers)

# # Create a new list containing only the even valuse of 'numbers'
# # for num in numbers:
# #   if num % 2 == 0:
# #     evens.append(num)
# evens = [num for num in numbers if num % 2 == 0]
# print(evens)

# # create a list of names that are properly capitalized and start with 's'
# names = ['Sarah', 'jorge', 'sam', 'frank', 'bob', 'sandy', 'shawn']

# s_names = [name.capitalize() for name in names if name[0].lower() == 's']
# print(s_names)

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
for x in range(5):
  	y.append(x+1)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for x in range(10):
	y.append(x**3)
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []
for item in a:
	y.append(item.capitalize())
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [ a for a in x if int(a)%2 == 0 ]

print(y)