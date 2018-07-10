# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [even_odd for even_odd in x if int(even_odd) % 2 == 0]

print(y)