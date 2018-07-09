# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
# x = [1, 2, 3, 4, 5, 6, 7, 8]

# What do you need between the square brackets to make it work?
y = [int(elem) for elem in x if int(elem) % 2 == 0]

print(y)

