x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(x)
x.append(4)
# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(x)
for num in y:
    x.append(num)
print(x)
# or concont with y + x but making sure each value
# feels safe.
# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(x)
del x[4]
print(x)
# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print(x)
x.insert(5, 99)
print(x)
# Print the length of list x
# YOUR CODE HERE
length = len(x)
print(f"amount of object in list: {length}")

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
y = []
for v in x.copy():
    i = v * 1000
    y.append(i)
print(y)
