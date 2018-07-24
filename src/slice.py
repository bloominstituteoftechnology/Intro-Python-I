a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])
#a[4] would not work due to needing always the second last element

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])
#using the : basically means "x to the end", so in this scenario, it means "starting from the third to last element, keep counting until the end"

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