"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

# * SOLUTIONS BELOW:
# * OPEN INTERPRETER && RUN: python3 02_datatypes.py

# ? TYPE() - RETURNS THE TYPE OF VALUE YOU ARE DEALING WITH.
# ? EX: <class 'int'> || <class 'str'>

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# ? INT() - CONVERTS A VALUE TO INTEGERS
print(
    x + int(y),
    type(x + int(y))
)

# Write a print statement that combines x + y into the string value 57

# ? STR() - CONVERTS A VALUE TO STRING
print(
    str(x + int(y)),
    type(str(x + int(y)))
)
