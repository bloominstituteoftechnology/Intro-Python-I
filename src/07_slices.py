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
print()
print(a[0:4])
indexOf = a[1]
print(indexOf)
# Output the second-to-last element: 9
print()
almostLast = a[-2]
print(almostLast)
# Output the last three elements in the array: [7, 9, 6]
print()
lastThree = a[3:]
print(lastThree)
# Output the two middle elements in the array: [1, 7]
print()
middle = a[2:4]
print(middle)
# Output every element except the first one: [4, 1, 7, 9, 6]
print()
noFirst = a[1:]
print(noFirst)

# Output every element except the last one: [2, 4, 1, 7, 9]
print()
noLast = a[:-1]
print(noLast)
# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print()
specialChar = s[7:12]
print(specialChar)