# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(x + [4])

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x +[4] + y[slice(1,3)])

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
y.insert(2, 99)
print(x + y)
# print(y.insert(2, 99))

# Print the length of list x
# YOUR CODE HERE
print(len(x))


# Print all the values in x multiplied by 1000
# YOUR CODE HERE

print([x[0]* 1000, x[1]*1000, x[2]*1000])