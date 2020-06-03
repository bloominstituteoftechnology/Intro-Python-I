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

print(slice(a[1]))

# Output the second-to-last element: 9
print(slice(a[4]))

# Output the last three elements in the array: [7, 9, 6]
slice_a = slice(3,6)
print(a[slice_a])

# Output the two middle elements in the array: [1, 7]
a_slice = slice(2,4)
print(a[a_slice])

# Output every element except the first one: [4, 1, 7, 9, 6]
except_first = slice(1,6)
print(a[except_first])

# Output every element except the last one: [2, 4, 1, 7, 9]
last_slice = slice(0, 5)
print(a[last_slice])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
hello_slice = slice(6,12)
print(s[hello_slice])