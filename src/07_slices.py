"""
Python exposes a terse and intuitive syntax for performing
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string.

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

import math

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4
print(a[1:2])

# Output the second-to-last element: 9
print(a[-2:-3:-1])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3::1])

# Output the two middle elements in the array: [1, 7]
print(a[2:-2])

"""
# I assume the above is what is expected but it will only work for an array of this length
# STRETCH: This will print the middle two elements in a given array (will be rounded DOWN if odd number of elements).
print(a[(math.floor(len(a)/2)-1):(math.floor(len(a)/2)+1)])
# STRETCH: This will print the middle two elements in a given array (will be rounded UP if odd number of elements).
print(a[(math.ceil(len(a)/2)-1):(math.ceil(len(a)/2)+1)])
# STRETCH: This will print the middle two (if EVEN # of elements) or three (if ODD # of elements) elements in a given array.
print(a[(math.floor(len(a)/2)-1):(math.ceil(len(a)/2)+1)])
"""

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(f'"{s[7:12]}"')
