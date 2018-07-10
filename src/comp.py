# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# This converts the numbers into strings. We want integers, so I'm converting them back.
z = list(map(int, x))


# What do you need between the square brackets to make it work?
y = [i for i in z if i%2 ==0]

print(y)

