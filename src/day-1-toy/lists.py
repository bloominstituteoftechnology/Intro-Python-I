# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# 1. Change x so that it is [1, 2, 3, 4]
x.append(4)
print('--- 1 ---')
print(x, '\n')

# 2. Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x += y
print('--- 2 ---')
print(x, '\n')

# 3. Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print('--- 3 ---')
print(x, '\n')

# 4. Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print('--- 4 ---')
print(x, '\n')

# 5. Print the length of list x
print('--- 5 ---')
print(len(x))

# Using a for loop, print all the element values multiplied by 1000
print('--- 6 ---')
for i in x:
    print(i * 1000)