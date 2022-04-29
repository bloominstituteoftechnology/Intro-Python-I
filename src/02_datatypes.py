"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
# print(x + y) python doesn't support operation that add string and intergers unlike javascript which will just concatenate the int to the string
# YOUR CODE HERE
print(x + int(y , 10))


# Write a print statement that combines x + y into the string value 57
# YOUR CODE HERE
print(str(x + int(y, 10)) + "57")