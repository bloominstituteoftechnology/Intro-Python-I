# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []

for i in range(1,6):
    y.append(i)

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []

for i in range(0,9):
    y.append(i**3)

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []

for e in a:
    y.append(e.upper())

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?

y = [e for e in x if int(e) % 2 == 0]

print(y)

