# For the exercise, look up the methods and functions that are available for
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
print(x+y)


# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
y.remove(8)
i = x + y
print(i)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
i.insert(5, 99)
print(i)

# Print the length of list x
# YOUR CODE HERE
r = len(x)
print(r)
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for u in x:
    print(u * 1000)
