"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
#    0  1  2  3  4  5
a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[3:6])

# Output the two middle elements in the array: [1, 7]
#print(a[:2], a[:3])
mid = slice(2, 4)
print(a[mid])

# Output every element except the first one: [4, 1, 7, 9, 6]
firstNum = slice(1, 6)
print(a[firstNum])

# Output every element except the last one: [2, 4, 1, 7, 9]
lastNum = slice(1, 5)
print(a[lastNum])

# For string s...
#    0,1,
s = "Hello, world!"

# Output just the 8th-12th characters: "world"
getWorld = slice(7, 12)
print(s[getWorld])