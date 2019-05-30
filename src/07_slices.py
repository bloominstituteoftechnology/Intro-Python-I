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
print("the whole array:", a[:])
print("output the second element, four:", a[1])

# Output the second-to-last element: 9
print("second to last element:", a[-2])

# Output the last three elements in the array: [7, 9, 6]
print("the last three elements:", a[3:])

# Output the two middle elements in the array: [1, 7]
print("the two middle (only) elements:", a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print("every element except the first:", a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print("every element except the last:", a[0:5])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"

removed = s[:-1]
print("removed exclamation:", removed)
split = removed.split(',')
print("split:", split)
back = split[1]
print("just 8th-12th characters:", back)


#z = s.split(',')
#print(z)
#front = z[0].split(',')
#print("front", front)
#back = z[1].split(',')
#print("back", back)


#new_back = ','.join(back)
#print("new_back is:", new_back)
#empty_arr = []
#world  = empty_arr.append(new_back)
#print(empty_arr[:-1])