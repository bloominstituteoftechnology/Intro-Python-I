# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

l = [1,2,3,4,5]
y = [i for i in l]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
n = [0,1,2,3,4,5,6,7,8,9]
y = [i**3 for i in n]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [i.upper() for i in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [i for i in x if int(i)%2 == 0]

print(y)

