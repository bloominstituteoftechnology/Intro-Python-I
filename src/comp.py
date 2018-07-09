# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
for x in x:
    if(int(x) % 2) == 0:
        y = [x]
        print(y)

