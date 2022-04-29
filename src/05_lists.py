# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]
print("\nx = ", x)

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print("\nChange x so that it is [1, 2, 3, 4]")
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print("\nchange x so that it is [1, 2, 3, 4, 8, 9, 10]")
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print("\nChange x so that it is [1, 2, 3, 4, 9, 10]")
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print("\nChange x so that it is [1, 2, 3, 4, 9, 99, 10]")
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE
print("\nlength of list x: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("\nall the values in x multiplied by 1_000:\n")
for i in x:
    print(i * 1_000)