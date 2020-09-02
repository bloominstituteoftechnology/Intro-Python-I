# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
# or x.insert(3, 4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

# Method 1 using +
# x = x+y

# Method 2 append()
# for i in y:
#     x.append(i)

# Method 3 Using list comprehension
# combined_list = [i for k in [x,y] for i in k]
# print(combined_list)

# Method 4 using extend
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.pop(4)

# Method 2
# del x[4]

# Method 3
# x.remove(8)

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
for i in x:
    print(i*1000)
