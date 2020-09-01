# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend([n for n in y])

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(-1, 99)

# Print the length of list x
# YOUR CODE HERE
length = len(x)

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
list_comp = [n * 1000 for n in x]


if __name__ == "__main__":
    print(x)
    print('-----------------------')
    print(length)
    print('-----------------------')
    print(list_comp)
    print('-----------------------')
