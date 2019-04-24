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
# x = x + y
# x += y
for item in y:
    x.append(item)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE 
# print(x.pop(4))
for ind, val in enumerate(x):
    if val == 8:
        del x[ind]
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE 
# x.insert(5, 99)
# x.insert((len (x) - 1, 99)
# x.insert(-1, 99)
def stringDouble(number, array):
    for ind, val in enumerate(array):
        if val == number:
            result = str(val) + str(val)
            array.insert(ind + 1, int(result))
            print(x)
            break

stringDouble(9, x)
# Print the length of list x
# YOUR CODE HERE 

print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

def mult(array):
    newArray = []
    for x in array:
        x *= 1000
        newArray.append(x)
    print(newArray)

mult(x)

# for i in x:
#     print(i * 1000)