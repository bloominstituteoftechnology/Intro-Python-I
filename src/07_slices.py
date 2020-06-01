"""
Python exposes a terse and intuitive syntax for performing
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string.

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:*
"""

a = [2, 4, 1, 7, 9, 6]
print("the list equals" + str(a))
# Output the second element: 4:
print("output of the second element is: " + str(a[1]))

# Output the second-to-last element: 9
x = len(a) - 2
print("output of the second-to-last element is: " + str(a[x]))

# Output the last three elements in the array: [7, 9, 6]
print("output of the last three elements of the list are: " + str(a[-3:]))

# Output the two middle elements in the array: [1, 7]
first_half = int((len(a) / 2) - 1)  # inclusive start
second_half = int((len(a) / 2) + 1)  # non-inclusive ending
# print("first list_middle is: " + str(a[first_half])) # Testing to see what the inclusive start would be (1)
# print("second list_middle is: " + str(a[second_half])) # Testing to see what the exclusive end would be (9)
print("The middle of the list is: " + str(a[first_half: second_half]))

# Output every element except the first one: [4, 1, 7, 9, 6]
# the list starts at item#2/elemnt 1 (not zero)
print("The list except the first element is: " + str(a[1:]))

# Output every element except the last one: [2, 4, 1, 7, 9]
print("The list except the last element is: " + str(a[:len(a)-1]))  # thi

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print("The 8th-12th characters of 'Hello, world!' are: " + str(s[7:12]))
