"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [1, 2, 3, 4, 5]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

cubed = []
for x in range(10):
    cubed.append(x ** 3)

print(cubed)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = ["foo".upper(), "bar".upper(), "baz".upper()]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.
#listonums = [1, 0, 4, 8, 12, 16, 9, 7]

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work? 
# I got it to do something but not within the brackets and not what I expected.
y = [n for n in x if int(n) % 2 == 0]

# # iterating each number in list 
# for num in x: 
      
#     # checking condition 
#     if num % 2 == 0: 
#        print(num, end = " ")



print(y)