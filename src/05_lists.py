# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# # YOUR CODE HERE
#x.append(4)
x.insert(3, 4)
print(x)

# # Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# # YOUR CODE HERE
# for i in y:
#     x.append(i)
# print(x)
# print(x.extend(y))

x_y = x + y
print(x_y)
# # Change x so that it is [1, 2, 3, 4, 9, 10]
# # YOUR CODE HERE
# print(x_y.remove(8))
del x_y[4]
print(x_y)

# # Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# # YOUR CODE HERE
#print(x_y.insert(5, 99))
x_y.insert(5, 99)
print(x_y)

# # Print the length of list x
# # YOUR CODE HERE
print(len(x_y))

# print(len(x))
# # Print all the values in x multiplied by 1000
# # YOUR CODE HERE
# multiplied = [i * 10000 for i in x_y]
# print(multiplied)

# multiplied = []
# for i in x_y:
#     multiplied.append(i * 1000)
# print(multiplied)


# import pandas as pd
# t = pd.Series(x_y)
# print((t * 1000).tolist())


# import numpy as np 

# new_list = np.array(x_y)

# print(new_list * 1000)

new_item = x_y
new_item[:] = [x * 1000 for x in new_item] #very pythonic
print(new_item)