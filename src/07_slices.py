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
print(a[1:2])

# Output the second-to-last element: 9
print(a[len(a) - 2 : len(a) - 1])

# Output the last three elements in the array: [7, 9, 6]
print(a[len(a) - 3 : ])

# Output the two middle elements in the array: [1, 7]
# I want this one to be dynamic
if len(a) % 2 == 0:
    middle = a[len(a) // 2]
    middle_lower = a[len(a) // 2 - 1]
    print([middle_lower, middle])
else:
    middle = a[len(a) // 2]
    print(middle)
# and again using slice
print(a[2:4])


# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:len(a) - 1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(f"\"{s[7:12]}\"")
