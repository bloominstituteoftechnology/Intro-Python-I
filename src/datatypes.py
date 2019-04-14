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
def add_ints(num1, num2):
    """
    What are the types in this problem?
        Ideally, integers.
    Do I have to convert the types?
        If given anything other than integers, yes. This can be handled by converting all arguments that are passed in or
        pushing all arguments through if statements to check for type, then converting based on that.
    
    Pseudocode:
        convert the arguments to integers
        add the arguments together and return the result
    """
    print(int(num1) + int(num2))
add_ints(x, y)

# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
def add_strs(str1, str2):
    """
    What are the types in this problem?
        Strings.
    Do I have to convert the types?
        If given anything other than strings, yes. This can be handled by converting all arguments that are passed in or
        pushing all arguments through if statements to check for type, then converting based on that.
    
    Pseudocode:
        convert the arguments to strings
        add the arguments together and return the result
    """
    print(str(str1) + str(str2))
add_strs(x, y)