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

# YOUR CODE HERE


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
# 2
# https://github.com/LambdaSchool/Intro-Python-I/blob/master/src/02_datatypes.py


x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

print(x + int(y), "is the combined int.")


# Write a print statement that combines x + y into the string value 57

print(str(x) + y, "is the combined str.")