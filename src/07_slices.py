"""
Python exposes a terse and intuitive syntax for performing
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string.

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
a = [2, 4, 1, 7, 9, 6]

"""
The slice() function returns a slice object that can be used to slice strings,
lists, tuple etc.
e.g., below:
"""
# Output the second element: 4:
print('The second slement is:', a[1], '\n')
print('+-------------------------------+')
# Output the second-to-last element: 9
print('The second-to-last element is:', a[4], '\n')
print('+-------------------------------+')

# Output the last three elements in the array: [7, 9, 6]
print('The last three elements in the arrary are:', a[3:6], '\n')
print('+-------------------------------+')

# Output the two middle elements in the array: [1, 7]
print('The two middle elements in the arrar are:', a[2:4], '\n')
print('+-------------------------------+')

# Output every element except the first one: [4, 1, 7, 9, 6]
print('Every element except the first:', a[1:], '\n')
print('+-------------------------------+')

# Output every element except the last one: [2, 4, 1, 7, 9]
print('Every element except the last one:', a[:-1], '\n')
print('+-------------------------------+')

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print('Last Word:', s[7:12])
