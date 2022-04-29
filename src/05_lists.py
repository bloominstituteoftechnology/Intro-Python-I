# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
def list_append(x):

    x.append(4)
    print(x)

    return x

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
def list_concat(x, y):

    x = x + y

    print(x)
    
    return x

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
def list_rem(x):

    x.remove(8)

    print(x)

    return x

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
def list_insert(x):

    x.insert(5, 99)
    print(x)

    return x

# Print the length of list x
# YOUR CODE HERE
def list_length(x):

    print(len(x))

    return x

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
def list_val_multiplier(x):

    [print(val*1000) for val in x]

if __name__ == "__main__":
    x = list_append(x)
    x = list_concat(x, y)
    x = list_rem(x)
    x = list_insert(x)
    x = list_length(x)
    list_val_multiplier(x)