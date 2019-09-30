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
iObject = slice(1,3,2)
print(a[iObject])

# Output the second-to-last element: 9
iObject = slice(4,6,2)
print(a[iObject])

# Output the last three elements in the array: [7, 9, 6]
iObject = slice(3,6,1)
print(a[iObject])

# Output the two middle elements in the array: [1, 7]
iObject = slice(3,5,1)
print(a[iObject])

# Output every element except the first one: [4, 1, 7, 9, 6]
iObject = slice(1,6,1)
print(a[iObject])

# Output every element except the last one: [2, 4, 1, 7, 9]
iObject = slice(0,5,1)
print(a[iObject])
print()

# For string s......

s = "Hello, world!"

# Output just the 8th-12th characters:  "world" ...
sObject = slice(7,12,1)
print(s[sObject])