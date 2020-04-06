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
secondElement = a[1:2]
print(secondElement)

# Output the second-to-last element: 9
secondToLast = a[len(a)-2:len(a)-1]
print(secondToLast)

# Output the last three elements in the array: [7, 9, 6]
lastThree = a[len(a)-3:]
print(lastThree)

for num in lastThree:
    print(num)

# Output the two middle elements in the array: [1, 7]
midTwo = a[len(a)//2 - 1: len(a)//2 + 1]
print(midTwo)

# Output every element except the first one: [4, 1, 7, 9, 6]
exceptFirst = a[1:]
print(exceptFirst)

# Output every element except the last one: [2, 4, 1, 7, 9]
exceptLast = a[:len(a)-1]
print(exceptLast)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
eightToTwelfth = s[7:12]
print(eightToTwelfth)