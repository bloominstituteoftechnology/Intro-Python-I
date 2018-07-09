# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
def even(): 
    y = []
    for index in range(len(x)): 
        if (int(x[index]) % 2 == 0): 
            y.append(x[index])
    
    return y

print(even())

