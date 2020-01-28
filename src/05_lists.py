# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)
output = [1,2,3,4]

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)
output = [1, 2, 3, 4, 8, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.pop(4)
print(x)
output= [1, 2, 3, 4, 9, 10]

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)
output = [1, 2, 3, 4, 9, 99, 10]

# Print the length of list x
len(x)
output = 7#items

# Print all the values in x multiplied by 1000
mult_by_1000 = [i * 1000 for i in x]
print(mult_by_1000)
output = [1000, 2000, 3000, 4000, 9000, 99000, 10000]

