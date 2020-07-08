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
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])
# Alt. syntax: print(a[3:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])


# --------------------------------------------------------------------------------
# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:-1])

# Alt. method #1: 
print(s[-6:-1])

# Alt. method #2: Python string split() method:
print(s.split()[-1][:-1])

# Just for practice w/ RegEx:

# Alt. method #3: RegEx (most concise way):
import re
result = re.findall(r"\w+", s)[-1]
print(result)

# Alt. method #4: RegEx (less concise because re.split() returns "" at end...):
tokens = re.split(r"[\W] *", s)
answer = list(filter(lambda x: x != "", tokens))[-1]
print(answer)
