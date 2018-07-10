# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# [command here]
x.extend([8, 9, 10])
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# [command here]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# [command here]
x.insert(-1, 99)
print(x)

# Print the length of list x
# [command here]
print(len(x))

# Using a for loop, print all the element values multiplied by 1000

elements = [1, 2, 3, 4, 9, 99, 10]

for x in elements:
    print(x*1000)

for i in range(10, 0, -1):
    print(i)