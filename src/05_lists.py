# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# x.append(4)
# print("updated list :", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# x.extend(y)
# print(str(x))

# Change x so that it is [1, 2, 3, 4, 9, 10]
# x.extend((4, 9, 10))
# print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# x.extend([4, 9, 99, 10])
# print(x)

# Print the length of list x
# print(len(x))

# Print all the values in x multiplied by 1000
def multiplyList(x):
    result = 1
    for x in x:
        result = result * 1000
    return result
print(multiplyList(x))