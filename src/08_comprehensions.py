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
y = [x+1 for x in range(5)]
#y = list(map(lambda x: x+1, range(5)))
print(y)

#Or, more fully written out:
y=[]
for n in range(5):
    y.append(n+1)
print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
for n in range(10):
    y.append(n**3)
print(y)

#OR...
#y = list(map(lambda x: x**3, range(10)))
y = [x**3 for x in range(10)]
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []
for e in a:
    y.append(e.upper())
print(y)

#or
y = [e.upper() for e in a]
print(y)


# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

#x = ["25","19","12",16,42,"9"] <-- Test values
y = []
for n in x:
    if int(n)%2 == 0:
        y.append(int(n))

print(y)

# What do you need between the square brackets to make it work?
y = []
y = [int(n) for n in x if int(n)%2==0]
print(y)
