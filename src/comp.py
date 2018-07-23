# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
i = 0
while i != 5:
    y.append(i)
    i += 1
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
i = 0
while i != 10:
    y.append(i * i * i)
    i += 1
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []
i = 0
while i != len(a):
    y.append(a[i].upper())
    i += 1
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = []
for each in x:
    each = int(each)
    if each % 2 == 0:
        y.append(each)
print(y)
