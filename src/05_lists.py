# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]

# Will be appending to the list 
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)

print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# Will be removing the 8 out of the list
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# adding the number 99 at the next to the last element
x.insert(len(x)-1, 99)
print(x)

# Print the length of list x
print(f"The length of x is: {len(x)}")

# Print all the values in x multiplied by 1000
# doing a loop to print all the values of x times 1000
print("These are all the values of x times 1000:")
for val in x:
    print(val * 1000)