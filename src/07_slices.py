"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
# a[start:stop:step] # start through not past stop, by step
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])