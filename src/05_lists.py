# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]

# YOUR CODE HERE 
x.append (4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE 
for y in range(3, 11):
  x.append(y) 
for j in range(5,8):
  x.remove(j)

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 

x.insert(7,99)
  
print(x)

# Print the length of list x
# YOUR CODE HERE 
print(len(x),"36")


# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for x in range(0,len(x)):
  print(x *1000)