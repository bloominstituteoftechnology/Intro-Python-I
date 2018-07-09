# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
# [command here]
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x = x + y
# [command here]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.pop(4)
# [command here]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
# [command here]
print(x)

# Print the length of list x
# [command here]
print(len(x))

# Using a for loop, print all the element values in x multiplied by 1000
for a in range(len(x)): 
    if (a == len(x)-1): 
        print(x[a] * 1000)
    else: 
        print(x[a] * 1000, end=' ')

# Using a for loop, print all the element values in y multiplied by 1000
for b in y: 
    print(b * 1000, end=' ')
