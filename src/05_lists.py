# For the exercise, look up the methods and functions that are available for use
# empty list
# p = [10, 6, 60, 5]
# p.append(77)
# print(p)
#
# # for loop
# for e in p:
#     print(e)
#
# for (index, e) in enumerate(p):
#     print(f'{index}: {e})

# list comprehensions
numbers = [1, 2, 3, 4, 5]
# squares = []
# for n in numbers:
#     squares.append(n * n)
# squares = [n*n for n in numbers]
# print(squares)

# create a new list containing only even number
# evens = []
# for n in numbers:
#     if n % 2 == 0:
#         evens.append(n)

# evens = [n for n in numbers if n % 2 == 0]
# print(evens)

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
for num in y:
    x.append(num)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.pop()
x.append(99)
x.append(10)
print(x)

# Print the length of list x
# YOUR CODE HERE
print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
multiplied = [num*1000 for num in x]
print(multiplied)
