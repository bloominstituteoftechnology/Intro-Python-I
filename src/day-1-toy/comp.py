# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
y = [i for i in range(1, 6)]
    print(y)
#Or
y = []
for i in range(1,5):
    y.append(i)

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
[i**3 for i in y]
print(y)
#OR
y = [i**3 for i in range(10)]
    print(y)
# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]
lower = [x.lower() for x in a]
print(lower)                
#  //['foo', 'bar', 'baz']

lower = [x.upper() for x in a]
print(lower)                 
# //['FOO', 'BAR', 'BAZ']
y = [word[0].upp() + word[i] for word in a]
print(y) 
#first letter cap

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [i for i in x if int(i) % 2 == 0]
    print(y)

