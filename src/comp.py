# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [x % 2]

# for i in y:
#     if y % 2 == 0
#         print(y)
#     else:
#         print("You fail at life!")

print(y)

