# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [n for n in [1, 2, 3, 4, 5] ]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [n*n*n for n in [1,2,3,4,5,6,7,8,9]]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [n.upper() for n in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# # What do you need between the square brackets to make it work?

#NOT WORKING
y = [n for n in x if int(n) % 2 == 0]

print(y)



##EXAMPLE from website online
# Program to filter out only the even items from a list

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(filter(lambda x: (x%2 == 0) , my_list))

# # Output: [4, 6, 8, 12]
# print(new_list)
