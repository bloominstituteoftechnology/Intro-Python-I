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
print("second element: " + str(a[1]))

# Output the second-to-last element: 9
print("second-to-last: " + str(a[len(a) - 2]))

# Output the last three elements in the array: [7, 9, 6]
length = len(a)
start = length - 3
for val in range(start, length):
    print("last three: " + str(a[val]))

# Output the two middle elements in the array: [1, 7]
middle = length // 2
for val in range(middle - 1, middle + 1):
    print("middle: " + str(a[val]))

# Output every element except the first one: [4, 1, 7, 9, 6]
for val in range(1, length):
    print("all but first" + str(a[val]))

# Output every element except the last one: [2, 4, 1, 7, 9]
for val in range(0, length - 1):
    print("all but last: " + str(a[val]))

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
for val in range(7, 12):
    print("8 - 12: " + str(s[val]))
