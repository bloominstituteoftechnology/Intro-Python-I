# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
def add(x):
    x.append(4)
    return x    
print(add(x))

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
def add_y(x, y):
    for i in (y):
        x.append(i)
    return x
    
print(add_y(x, y))
# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
def sub_8(x):
    li = []
    for i in (x):
        if i != 8:
            li.append(i)
    return li
print(sub_8(x))

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
def add_99(x):
    del x[4]
    del x[-1]
    x.append(99)
    x.append(10)
    return x


print(add_99(x))

# Print the length of list x
# YOUR CODE HERE

print("length of x",len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
def mult(x):
    lis = []
    for i in x:
        lis.append(i * 1000)
    return lis
print(mult(x))
        