# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')
numsList = []
for num in x:
    n = int(num)
    numsList.append(n)
# What do you need between the square brackets to make it work?
y = []

for num in numsList:
    if num % 2 == 0:
        y.append(num)

print(y)