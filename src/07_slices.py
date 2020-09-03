"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
x = a[1:2]
print(x)

# Output the second-to-last element: 9
x = a[-2:-1]
print(x)

# Output the last three elements in the array: [7, 9, 6]
x = a[-3:]
print(x)

# Output the two middle elements in the array: [1, 7]
x = a[2:4]
print(x)

# Output every element except the first one: [4, 1, 7, 9, 6]
x = a[-5:]
print(x)

# Output every element except the last one: [2, 4, 1, 7, 9]
x = a[0:5]
print(x)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
x = s[7:12]
print(x)