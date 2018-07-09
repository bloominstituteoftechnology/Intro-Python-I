# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
print(x)

# What do you need between the square brackets to make it work?
y = [int(i) for i in x if int(i) % 2 == 0]

print(y)

