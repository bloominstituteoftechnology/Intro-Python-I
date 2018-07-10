# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

x = [int(i) for i in x]

# What do you need between the square brackets to make it work?
y = [i for i in x if i % 2 == 0]

print(y)
