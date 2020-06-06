"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [nums for nums in range(6) if nums > 0 < 6]

# for nums in range(6):
#     if nums == 0:
#         continue
#     y.append(nums)
print(y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [nums * nums * nums for nums in range(10)]

# for nums in range(10):
#     cubed_nums = nums * nums * nums
#     y.append(cubed_nums)
print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [el.upper() for el in a]

# for el in a:
#     y.append(el.upper())
print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [nums for nums in x if int(nums) % 2 == 0]

# for nums in x:
#     if int(nums) % 2 == 0:
#         y.append(nums)

# also need to turn turn the string values into integers

print(y)