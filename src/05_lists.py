# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x = [1, 2, 3]
x1 = x
x1 += [4,]
print(x1)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
y = [8, 9 ,10]
x.append(4)
x = x + y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x = [1, 2, 3]
ls = [4, 9, 99, 10]
x.extend(ls)
print(x)

# Print the length of list x
x = [1, 2, 3]
print(len(x))

# Print all the values in x multiplied by 1000
new_x = [i * 1000 for i in x]
print(new_x)
