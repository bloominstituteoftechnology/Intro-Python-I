# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
print("Append item to end of list")
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
print("Extend x with y")
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
print("Remove 8")
x.pop(4)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
print("Add 99")
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print("Length of x is: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("x values * 1000")
new_list = [i * 1000 for i in x]
print(new_list)