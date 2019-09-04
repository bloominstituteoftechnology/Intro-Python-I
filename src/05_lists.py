# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
## append works like push
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
## extends adds two arrays together
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
## remove third from last
x.pop(-3)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
## DONT FORGET COLON AFTER FIRST LINE OF for 
for z in x:
    print(z * 1000)