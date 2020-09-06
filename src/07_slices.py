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
# print(a[-2]) This print the second to last element of the array, no matter hon long the array is.
# print(a[:4]) This prints [2, 4, 1, 7]
# print(a[4:]) Starts at 4 and includes the las number of the array.

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

myArray = [2, 4, 1, 7, 9, 6]
myNewArray = []

for (index, numbers) in enumerate(myArray):
    if index >= len(myArray) - 3:
        myNewArray.append(numbers)
print(myNewArray)


# Output the two middle elements in the array: [1, 7]
print(a[2:4])
print(a[2:4:])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:5])
print(a[:6:2]) #This is includes all the negative numbers (wrap around) from -1, -2, -3, -4, -5 **** The third number shows how the steping should be. 
print(a[:-1])  #It prints the entire list up to the last number, we're just using the wrap around system with negative numbers using the negative index.

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])