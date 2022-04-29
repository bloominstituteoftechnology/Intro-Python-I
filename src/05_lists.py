# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# Append
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
#for i in y:
 #   x.append(i)
#print(x)

#extend
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
#x.pop(4)
x.remove(8)
#del x[4]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
new_x = [i * 1000 for i in x]
print(new_x)