# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# [command here]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# [command here]
x.extend(y) # meaningful 
# x = x + y cheap way of doing it.. 
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# [command here]
x.__delitem__(-3) # this one deletes by index ".remove(8)" removes by item if found
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# [command here]
x.insert(5, 99) # insert after current index depending on the direction of the indexes negative to positive
print(x)

# Print the length of list x
# [command here]
print(len(x))

# Using a for loop, print all the element values multiplied by 1000
for each in x:
    print("{0} multipled by 1000 equals {1}".format(each, each * 1000)) 