# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ")
y = []
oldarr = x.split(',')
for i in oldarr:
    if int(i) % 2 == 0:
        y.append(i)
    else:
        continue




# What do you need between the square brackets to make it work?



print(y)

