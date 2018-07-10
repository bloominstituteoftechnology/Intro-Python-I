# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [int(i) for i in x if int(i) % 2 == 0 ]

print(y)

"""
#x = input("Enter comma-separated numbers: ").split(',')
#Enter comma-separated numbers: 2,3,4,5,2,76,8,4,2,4,5
#>>> y = [int(i) for i in x if int(i) % 2 == 0 ]
#>>> print(y)
#[2, 4, 2, 76, 8, 4, 2, 4]
"""