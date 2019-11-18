# For the exercise, look up the methods and functions that are available for use
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
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
x.insert(5, 99)
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
newList = [i *1000 for i in x]
print(newList)



# https://developers.google.com/edu/python/lists
# https://www.quora.com/What-is-the-best-way-to-find-the-length-of-a-list-in-Python
# https://stackoverflow.com/questions/35166633/how-do-i-multiply-each-element-in-a-list-by-a-number/35166717