# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.insert(3,4)
print('Expected: [1, 2, 3, 4]                           - Result:',x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
print('Expected: [1, 2, 3, 4, 8, 9, 10]                 - Result:',x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print('Expected: [1, 2, 3, 4, 9, 10]                    - Result:',x + y[1:3])

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
y.insert(3, 99)
print('Expected: [1, 2, 3, 4, 9, 99, 10]                - Result:',x + y[1:2] + y[3:4] + y[2:3])

# Print the length of list x
# YOUR CODE HERE
print('Expected: 4                                      - Result:',len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HER
for i in range(len(x)):
    print('                                                 ',x[i] , ':Multiply by 1000 =' ,x[i]*1000)