# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x, '\n')

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
print('+---------------------+')
# YOUR CODE HERE
x = x + y
print(x, '\n')

# Change x so that it is [1, 2, 3, 4, 9, 10]
print('+---------------------+')
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
print('+---------------------+')
# YOUR CODE HERE
x.insert(5, 99)
print(x, '\n')

# Print the length of list x
print('+---------------------+')
# YOUR CODE HERE
print('Length of x:', len(x), '\n')
# Print all the values in x multiplied by 1000
print('+---------------------+')
# YOUR CODE HERE
print([i*1000 for i in x], '\n')
