"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""
#slice(start, end, step) start: starting position to start slice, end: where to end the slice, step: (optional) specifies the step of the slicing.

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
b = slice(1,2)
print("1:", a[b])

# Output the second-to-last element: 9
c = slice(4,5)
print("2:", a[c])

# Output the last three elements in the array: [7, 9, 6]
d = slice(3,6)
print("3:", a[d])

# Output the two middle elements in the array: [1, 7]
e = slice(2,4)
print("4:", a[e])

# Output every element except the first one: [4, 1, 7, 9, 6]
f = slice(1,6)
print("5:", a[f])

# Output every element except the last one: [2, 4, 1, 7, 9]
g = slice(0,5)
print("6:", a[g])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
h = slice(7,12)
print("7:", s[h])