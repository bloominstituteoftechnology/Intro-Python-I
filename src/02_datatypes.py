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

""" the gotcha here is y is a string and must be passed by an 
int() command in the print command to use it as a number"""

print(x + int(y))

# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
""" in this exersize we are to concatenate the two variables 
    as a string so str(x) must be used to turn x into a string"""

print(str(x) + y)
