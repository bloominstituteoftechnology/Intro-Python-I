# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
y = x + y
print(y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.append(9)
x.append(10)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x[5] += 89
x.append(10)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for i in x:
    print(i * 1000)