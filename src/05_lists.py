# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).
"""
append() is a method in python which adds
a single item to the existing list. In this case
a Four
"""
# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(x, '\n')

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
print('+---------------------+')
# YOUR CODE HERE
x = x + y
print(x, '\n')

# Change x so that it is [1, 2, 3, 4, 9, 10]
"""
remove() is an inbuilt function in Python that removes a given object
from the list.

 e.g., x.remove(8) removes the number eight.
"""
print('+---------------------+')
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
"""
the insert() is a method wich inserts an item at a given position.
 e.g., x.insert(8, 99) inserts the number 99 in position five.
"""
print('+---------------------+')
# YOUR CODE HERE
x.insert(5, 99)
print(x, '\n')

# Print the length of list x
"""
The len() method is used to find the length of the list in Python.
"""
print('+---------------------+')
# YOUR CODE HERE
print('Length of x:', len(x), '\n')
# Print all the values in x multiplied by 1000
print('+---------------------+')
# YOUR CODE HERE
print([i*1000 for i in x], '\n')
