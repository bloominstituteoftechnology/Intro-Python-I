# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE 
print("extend method:", x.extend([4]))

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
print("second extend method", x.extend(y))

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
index = 4
print("del delete 4th index method, return [1,2,3,4,9,10]", x[:index] + [9] + [10])

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 

#print("this is x:", x)
#print("inserting 99 into x using insert:", x.insert(6,99))    #WHY NOT WORKING?
print("inserting 99 into x using slice:", x[:6] + [99] + x[6:])  


# Print the length of list x
# YOUR CODE HERE 

print("length of x:", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

new_list = [i * 10 for i in x]
print("new list:", new_list)