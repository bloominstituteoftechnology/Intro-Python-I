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
#z = x
#x.pop()
#x.append(99)
#x.pop()

x.insert(5, 99)
#print(z)
print(x)

# Print the length of list x
print(len(x))

# YOUR CODE HERE

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
#print(x*1000)
new_list = []
    
iterable = iter(x)
for item in iterable:
    thousand = item*1000
    #print(thousand)
    #new_list = []
    new_list.append(thousand)
print(new_list)
