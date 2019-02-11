"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

# a[start:end]  items start through end-1
# a[start:]     items start through the rest of the array
# a[:end]       items from the beginning through end-1
# a[:]          a copy of the whole array

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
second_to_last = len(a) - 2
print(a[second_to_last])

# Output the last three elements in the array: [7, 9, 6]
last_three = len(a) - 3
print(a[last_three:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
except_last = len(a) - 1
print(a[:except_last])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])