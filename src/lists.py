# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
def insertnum():
    for num in x:
        if num == 9:
            # print(x.index(9) + 1)
            x.insert(x.index(9) + 1, 99)
insertnum()
print(x)

# Print the length of list x
# YOUR CODE HERE 
print("length of x: " + str(len(x)))
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
multiple = map(lambda z: z*1000, x )
numberbythou = list(multiple)
print(numberbythou)