# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]
if __name__=='__main__':
    # For the following, DO NOT USE AN ASSIGNMENT (=).

    # Change x so that it is [1, 2, 3, 4]
    x.append(4)
    print(x)

    # Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
    x.extend(y)
    print(x)

    # Change x so that it is [1, 2, 3, 4, 9, 10]
    x.extend(y[1:])
    print(x)

    # Change x so that it is [1, 2, 3, 4, 9, 99, 10]
    for k in (9, 99, 10):
        x.append(k)
    print(x)

    # Print the length of list x
    print(len(x))

    # Print all the values in x multiplied by 1000
    print([a*1000 for a in x])
