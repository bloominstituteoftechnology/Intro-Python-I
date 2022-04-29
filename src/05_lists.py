# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x = x + y
# # Alternative syntax;
# for item in y:
#     x.append(item)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(-1, 99)
print(x)

# Print the length of list x
print(f"Length of list x: {len(x)}")

# Print all the values in x multiplied by 1000
print("\nList x with all values multiplied by 1000:")
print(f"List comprehensions version: {[item * 1000 for item in x]}")

import numpy as np
x = np.array(x)
print(f"Numpy array version: {x * 1000}")
