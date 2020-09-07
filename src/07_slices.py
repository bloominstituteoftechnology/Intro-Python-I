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
print(a[1])

# Output the second-to-last element: 9
print(a[4])

# Output the last three elements in the array: [7, 9, 6]
print(a[3], a[4], a[5])

# Output the two middle elements in the array: [1, 7]
mid = slice(2, 4)
print(a[mid])

# Output every element except the first one: [4, 1, 7, 9, 6]
x = slice(1, 5)
print(a[x])

# Output every element except the last one: [2, 4, 1, 7, 9]
pop = slice(0, 4)
print(a[pop])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
world = slice(7, 12)
print(s[world])