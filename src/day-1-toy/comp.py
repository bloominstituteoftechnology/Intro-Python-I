# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [x for x in range(1,6)]
# for n in range(1, 6):
#     y.append(n)
# squares = [x for x in range(10)]

print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [x ** 3 for x in range(0,10)]
# for n in range(0, 10):
#     y.append(n ** 3)
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]
# for n in a:
#     y.append(n.upper())
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [n for n in x if int(n) % 2 == 0]
# for n in x:
#     if int(n) % 2 == 0:
#         y.append(n)
print(y)
