# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
[y.append(i) for i in range(1, 6)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
[y.append(pow(i, 3)) for i in range(0, 10)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []
[y.append(word.upper()) for word in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(", ")

# What do you need between the square brackets to make it work?
y = []
[y.append(even) for even in x if (int(even) % 2 == 0)]

print(y)

