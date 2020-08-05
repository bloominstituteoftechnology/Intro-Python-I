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
print(x + y)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.extend([9, 10])
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

print(x)

# Print the length of list x
# YOUR CODE HERE
for elem in x:
    print(elem)

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
multipleArray = []
for i in x:
    multipleArray.append(i * 1000)

    print(multipleArray)

# -------------------------- class work -----------------

# create an empty list
empty = []

# create a list with some numbers
nums = [10, 60, 20, 5]

# print out our list of numbers
print(nums)

# add a number to our "nums" list
nums.append(77)

print(nums)

# let's print oout every value in the "nums" list, one at a time

for elem in nums:
    print(elem)

# what if we want to iterate alone the length of a list 
# what if we want to iterate x number of times?
for n in range(2, 10):
    print(n)

# what if we want to iterate along the length of a list 
for i in range (lens(nums)):
    print(i, nums[i])

# another way to print out elements from a list with the associated index
# i is the index, v is the value
for value, index in enumerate(nums):
    print(index, value)