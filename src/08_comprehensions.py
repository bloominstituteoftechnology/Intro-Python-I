"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x**3 for x in range(10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
upperA = [str.upper() for str in a]
print(upperA)

# print(a[0].capitalize(), a[1].capitalize(), a[2].capitalize())


# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

print(x)

# What do you need between the square brackets to make it work?
y = [n for n in x if int(n) % 2 == 0]

# check if n is motified by 2 is equal to zero, 
# this wouldnt work because you cant mod a string as a int. so we have to cast the string in as an int

print(y)

# --------------- CLASS WORK

# check pic

# comprehensions allow us to write the above logic in  a much terse fashion

# Create a list of the square values of numbers in the range of 1-10
squares = []

for i in range(1, 11):
    squares_1.append(i**2)

# print(squares)

squares_2 = [i**2 for i in range(1,11)]

print(squares_1 == squares_2)

names = ["Nonye", "Lemuel", "Roz", "Nichoel", "Aster"]

# create a list containing only the names that start with "s"
# and also make sure all the names are properly capitalized
s_names = [name.capitlized() for name in names if name[0].lower() == "s"]

# for name in names:
    # check if the name starts with "s"
    # also 
    
