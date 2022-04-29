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
print(f"value of x is {x}")
print(f"value of y is {y}")

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
y_int = int(y)

print(f"integer addition: x + y = {x+y_int}")

# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
x_str = str(x)

print(f"string addition: x + y = {x_str+y}")
