# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print(f'Change x so that it is [1, 2, 3, 4] ==> {x}')

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
for num in y:
    x.append(num)
print(f'Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10] ==> {x}')

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(f'Change x so that it is [1, 2, 3, 4, 9, 10] ==> {x}')

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(4, 99)
print(f'Change x so that it is [1, 2, 3, 4, 9, 99, 10] ==> {x}')

# Print the length of list x
# YOUR CODE HERE
print(f'Print the length of list x ==> {len(x)}')
# Print all the values in x multiplied by 1000
# YOUR CODE HERE

print(f'Print all the values in x multiplied by 1000 ==> {list(map(lambda n: n*1000, x))}')