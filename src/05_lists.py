# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x)
print('\n')

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for i in y:
    x.append(i)
print(x)
print('\n')

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)
print(x)
print('\n')

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print(x)
print('\n')

# Print the length of list x
# YOUR CODE HERE
print(len(x))
print('\n')

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print([i*1000 for i in x])