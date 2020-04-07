# For the exercise, look up the methods and functions that are available for use
# with Python lists.
'''
Python List append()
Add a single element to the end of the list

Python List extend()
Add Elements of a List to Another List

Python List insert()
Inserts Element to The List

Python List remove()
Removes item from the list

Python List index()
returns smallest index of element in list

Python List count()
returns occurrences of element in a list

Python List pop()
Removes element at the given index

Python List reverse()
Reverses a List

Python List sort()
sorts elements of a list

Python List copy()
Returns Shallow Copy of a List

Python List clear()
Removes all Items from the List

Python any()
Checks if any Element of an Iterable is True

Python all()
returns true when all elements in iterable is true

Python ascii()
Returns String Containing Printable Representation

Python bool()
Converts a Value to Boolean

Python enumerate()
Returns an Enumerate Object

Python filter()
constructs iterator from elements which are true

Python iter()
returns an iterator

Python list()
creates a list in Python

Python len()
Returns Length of an Object

Python max()
returns the largest item

Python min()
returns the smallest value

Python map()
Applies Function and Returns a List

Python reversed()
returns the reversed iterator of a sequence

Python slice()
returns a slice object

Python sorted()
returns a sorted list from the given iterable

Python sum()
Adds items of an Iterable

Python zip()
Returns an iterator of tuples
'''
x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Print the length of list x
print(len(x))


# Print all the values in x multiplied by 1000

def times1000(n):
    return n * 1000


result = map(times1000, x)
print(result)

bigXlist = list(result)
print(bigXlist)

# List Comprehension is better (less code)
x1000 = [n * 1000 for n in x]
# ^^^^^^^^^ ^^^^^ ^^^^
# output    input   filter
print(x1000)
