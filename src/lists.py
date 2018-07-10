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
x.extend(y)
# could also do this --> x += y
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# [command here]
x.remove(8)
# or x.pop(<index>)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# [command here]
x.insert(5, 99)
print(x)

# Print the length of list x
# [command here]
print(len(x))

# Using a for loop, print all the element values multiplied by 1000
for num in x: 
   print(num*1000)
