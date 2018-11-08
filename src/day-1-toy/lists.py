# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).
# looked up datastructures here https://docs.python.org/2/tutorial/datastructures.html
# Change x so that it is [1, 2, 3, 4]
# [append]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# [extend]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# []
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# [insert]
x.insert(5, 99)
print(x)

# Print the length of list x
# [len]
print(len(x))

# Using a for loop, print all the element values multiplied by 1000
for number in x:
    print(number * 1000)
