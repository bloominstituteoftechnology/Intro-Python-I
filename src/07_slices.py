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
print(a[slice(1, 2, None)])

# Output the second-to-last element: 9
print(a[slice(-2, -1, None)])

# Output the last three elements in the array: [7, 9, 6]
print(a[slice(-3, None, 1)])

# Output the two middle elements in the array: [1, 7]
mid = int(len(a)/2) - 1
print(a[slice(mid, mid + 2)])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[slice(1, None, 1)])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[slice(None, -1, 1)])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[slice(7, -1, 1)])
