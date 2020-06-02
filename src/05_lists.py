# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]


# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)  # Complete!

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
print(x + y)  # Complete!

# Change x so that it is [1, 2, 3, 4, 9, 10]
for list_item in y[-2:]:
    x.append(list_item)
print(x)  # Complete!

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(-1, 99)
print(x)  # Complete!

# Print the length of list x
print('Length of x:', len(x))  # Complete!

# Print all the values in x multiplied by 1000
for list_item in x:
    print(list_item, '* 1000 =', list_item * 1000)  # Complete!
