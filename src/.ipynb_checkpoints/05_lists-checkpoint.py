# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).
x.insert(4,4)
# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
print(x)
x = x+y
# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
print(x)
f= x[0:4]
c= x[5:7]
x=f+c;
# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
print(x)
# list.insert(index, elem)
x.insert(5,99)
# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE