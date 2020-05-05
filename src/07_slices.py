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
b = a[1]
print(b)

# Output the second-to-last element: 9
c = a[-2]
print(c)

# Output the last three elements in the array: [7, 9, 6]
d = a[-3:]
print(d)

# Output the two middle elements in the array: [1, 7]
e = a[2:-2]
print(e)

# Output every element except the first one: [4, 1, 7, 9, 6]
f = a[1:]
print(f)

# Output every element except the last one: [2, 4, 1, 7, 9]
g = a[:-1]
print(g)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
h = s[7:12]
print(h)