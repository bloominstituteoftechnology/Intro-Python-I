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
# for x in range(5):
#     y.append(x)
# y.remove(0)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

z = [x**3 for x in range(10)]
# for cube in range(10):
#     z.append(cube**3)
print(z)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

capitol = [x.upper() for x in a]
# for up in a:
#     capitol.append(up.upper())
print(capitol)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("0,1,2,3,4,5,6,7,8,9").split(',')

# What do you need between the square brackets to make it work?
y = [z for z in x if int(z)%2==0]
# for i in x:
#        if int(i) % 2 == 0:
#         y.append(i)
print(y)
