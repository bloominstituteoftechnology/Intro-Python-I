# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]

x.append(4)
print('x added ==>:', x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]

x.extend(y)
print('extended list==>:', x)

# Change x so that it is [1, 2, 3, 4, 9, 10]

# del(x[4])
x.remove(8)
print('8 is  removed ==>:', x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]

# x.insert(-1, 99)
x.insert(len(x)-1, 99)
print('99 is added ==>:', x)

# Print the length of list x

print(len(x))

# Using a for loop, print all the element values multiplied by 1000

x = [element*1000 for element in x]
for element in x:
    print(element)
