# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
for i in range(1, 6):
    y.append(i)
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = []
for i in range(10):
    y.append(i**3)

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
y = []
for i in a:
    y.append(i.upper())

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input([1,2,3,4,5,6,7,8,9]).split(',')

# What do you need between the square brackets to make it work?
for i in x:
    if(true):
        y.append(i)
y = [1]

print(y)
