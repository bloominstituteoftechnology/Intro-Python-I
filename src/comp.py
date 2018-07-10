# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

intlist = list(map(int, x))

# What do you need between the square brackets to make it work?
y = [i for i in intlist if i % 2 == 0]
print(y)
