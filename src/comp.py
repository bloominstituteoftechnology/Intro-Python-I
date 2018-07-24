# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = []
value = 1
for x in range(5):
    y.append(value)
    value += 1
print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
value = 0
for x in range(10):
    cube = value ** 3
    y.append(cube)
    value += 1

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = []

for word in a:
    y.append(word[0].upper() + word[1:])
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = list(input("Enter comma-separated numbers: "))
y = []

for number in range(len(x)):
    if number % 2 == 0:
        y.append(number)
        
print(x)
print(y)

