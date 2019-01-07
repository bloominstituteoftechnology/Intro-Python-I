x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [number for number in x if int(number)%2==0]

print(y)