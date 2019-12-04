# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# YOUR CODE HERE 
# append is a method that modifies the existing list. It doesn't return a new list -- it returns None, like most methods that modify the list.
print('LISTS', x.append(4))
# print('LISTS', x.insert(4, 4))

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 

print('LISTS 2', x.extend(y))

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
print('LISTS 3', x.remove(8))

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
print('LISTS 4', x.insert(5, 99))

# Print the length of list x
# YOUR CODE HERE 
print(len(x))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
#by index
multiplied_by_1000 = [i * 1000 for i in x]
print(multiplied_by_1000)