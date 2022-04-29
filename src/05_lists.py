# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(x[len(x) - 1] + 1)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(len(x) - 1, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(f"Count of x: {len(x)}")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
newX = []
for val in x:
    newX.append(val * 1000)
print(newX)