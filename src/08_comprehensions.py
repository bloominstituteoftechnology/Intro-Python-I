"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.

new_list = [expression for member in iterable]
Every list comprehension in Python includes three elements:

expression is the member itself, a call to a method, or any other valid expression that returns a value. 
In the example above, the expression i * i is the square of the member value.
member is the object or value in the list or iterable. 

In the example above, the member value is i.
iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. 
In the example above, the iterable is range(10).
Because the expression requirement is so flexible, a list comprehension in Python works well in many places where you would use map().


"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [x for x in range(6) if x > 0]
print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
nums = [x for x in range(10)]
y = [x**3 for x in nums]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [x.upper() for x in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

""" 
Whatever you enter as input, input function convert it into a string. 
if you enter an integer value still input() function convert it into a string. 
You need to explicitly convert it into an integer


if I do [i for i in x if int(i) % 2 == 0] it gives me string in array ['2']; have to convert to integer on both i's
"""

x = input("Enter comma-separated numbers: ").split(',')

 y = [int(i) for i in x if int(i) % 2 == 0]

# What do you need between the square brackets to make it work?


print(y)