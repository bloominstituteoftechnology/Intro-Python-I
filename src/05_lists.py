# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
# YOUR CODE HERE 
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x = x + y
# YOUR CODE HERE 
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
del x[-3]
# YOUR CODE HERE 
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
# YOUR CODE HERE 
print(x)

# Print the length of list x
len(x)
# YOUR CODE HERE 

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for i in x:
    print(i * 1000)