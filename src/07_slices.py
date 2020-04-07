"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string.

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following.
"""

a = [2, 4, 1, 7, 9, 6]

# output the second element: 4
print(a[2])

# output the second-to-last element: 9
print(a[-1])

# output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# output the two middle elements in the array: [1, 7]
print(a[2:4])

# output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-2])

# output just the 8th-12th characters: 'world'
s = 'Hello, world!'

print(s[7:12])