"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
# Do a For in loop in one line and a regular For in loop.

y = [n for n in range(1, 6)]  # Same line For in loop.
print ("This is the short version:", y)

#Long version:
y1 = []
for num in range(1, 6):
    y1.append(num)
    print("This is the long version:", y1)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [n**3 for n in range(10)]
print("This is the short version:", y)

#Long version:
y2 = []

for num1 in range(10):
    y2.append(num1 ** 3)
    print("This is my long version", y2)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]
print("This is the short version:", y)

# The long version:
a1 = ["foo", "bar", "baz"]
y3 = []
for word in a1:
    y3.append(word.upper())
    print("This is the long version:", y3)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

print("Please enter a number:")
x = input("Enter comma-separated numbers: ").split(',')
print(x)

# What do you need between the square brackets to make it work?
y = [num for num in x if int(num) %2 == 0]
#print(y)