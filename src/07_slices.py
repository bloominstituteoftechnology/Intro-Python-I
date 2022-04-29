"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]
print("Original: ", a)

print("\nOutput the second element: 4:")
print(a[1])

print("\nOutput the second-to-last element: 9")
print(a[-2])

print("\nOutput the last three elements in the array: [7, 9, 6]")
print(a[3:])

print("\nOutput the two middle elements in the array: [1, 7]")
print(a[2:4])

print("\nOutput every element except the first one: [4, 1, 7, 9, 6]")
print(a[1:])

print("\nOutput every element except the last one: [2, 4, 1, 7, 9]")
print(a[:-1])

# For string s...

s = "Hello, world!"
print("\nOriginal: ", s)

print("\nOutput just the 8th-12th characters: 'world'")
print(s[slice(7,12)])
print(s[slice(7,None)])