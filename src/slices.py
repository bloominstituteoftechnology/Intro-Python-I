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
slice = a[1:2]
print(slice)

# Output the second-to-last element: 9
slice2 = a[4:5]
print(slice2)

# Output the last three elements in the array: [7, 9, 6]
slice3 = a[3:6]
print(slice3)

# Output the two middle elements in the array: [1, 7]
middle = a[2:4]
print(middle)

# Output every element except the first one: [4, 1, 7, 9, 6]
notfirst = a[1:6]
print(notfirst)

# Output every element except the last one: [2, 4, 1, 7, 9]
notlast = a[0:5]
print(notlast)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
newworld = s[7:12]
print(newworld)