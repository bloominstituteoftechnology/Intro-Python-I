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
x.insert(5,99)
print(x)

# Print the length of list x
# YOUR CODE HERE
length = len(x)
print(length)

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
# printing the list using loop 
for a in range(len(x)): 
    print (x[a] * 1000)



# 1. 
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

# prints out 1,2,3
for item in mylist:
    print(item)

# 2. if index doesn't exist, youll get an out of range exception.
x = 1
y = 2

x_list = [x] * 10
print(x_list)

y_list = [y] * 10
print(y_list)

combined = y_list + x_list
print(combined)




