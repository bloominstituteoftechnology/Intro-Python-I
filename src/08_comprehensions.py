"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.

[<map expression] for <name> in <sequence expression> if <filter expression>]
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

# y = []
# for num in range(6):
#     y.append(num ** 1)
# print (y)

y = []
for item in range(1, 6):
    y.append(item)
print(y)   
# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = []
start = 1
end = 9
for count in range(start, end + 1): 
    y.append (count ** 6)

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

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [num for num in x if int(num) % 2 == 0]

print(y)




## Intro to Python 3 Notes

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]
y = [item for item in  range(1, 6)]
print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
def cube_something(n):
    return n ** 3
y = [cube_something(item) for item in range(10)]  

# y = [item **3 for item in range(10)]
# for item in range(10):
#     y.append(item ** 3)
print(y)